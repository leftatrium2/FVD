import { defineStore } from 'pinia'
import { ref } from 'vue'
import request from '@/utils/request'

export const useUserStore = defineStore('user', () => {
  // 从localStorage初始化token
  const token = ref<string>(localStorage.getItem('token') || '')
  const userInfo = ref<any>(localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo')!) : null)
  const isLoggedIn = ref<boolean>(!!token.value)

  const setToken = (newToken: string) => {
    token.value = newToken
    isLoggedIn.value = !!newToken
    // 持久化到localStorage
    if (newToken) {
      localStorage.setItem('token', newToken)
    } else {
      localStorage.removeItem('token')
    }
  }

  const setUserInfo = (info: any) => {
    userInfo.value = info
    // 持久化到localStorage
    if (info) {
      localStorage.setItem('userInfo', JSON.stringify(info))
    } else {
      localStorage.removeItem('userInfo')
    }
  }

  const logout = async () => {
    try {
      // 调用后台退出登录接口
      await request.get('/login/logout')
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      // 无论接口是否成功，都清除本地状态
      token.value = ''
      userInfo.value = null
      isLoggedIn.value = false
      // 清除localStorage
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
    }
  }

  return {
    token,
    userInfo,
    isLoggedIn,
    setToken,
    setUserInfo,
    logout
  }
})
