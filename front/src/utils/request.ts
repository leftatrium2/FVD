import axios from 'axios'
import { message } from 'ant-design-vue'
import { useUserStore } from '@/store/user'
import type { Router } from 'vue-router'
import i18n from '@/locales'

/**
 * 获取国际化文本
 * @param key - 翻译key
 * @returns 翻译后的文本
 */
const t = (key: string): string => {
  return i18n.global.t(key)
}

// 创建axios实例
const request = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API || 'http://localhost:9002',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    // 从用户store获取token
    const userStore = useUserStore()
    const token = userStore.token
    
    // 如果token存在，添加到请求头
    if (token) {
      config.headers['token'] = token
    }
    
    return config
  },
  (error) => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    const res = response.data
    
    // 如果返回的code不是0，说明请求失败
    if (res.code !== 0) {
      // 根据不同的错误码进行处理
      if (res.code === 1001 || res.code === 1002 || res.code === 1112) {
        // token失效或未登录 (1112: LOGIN_ERR_TOKEN_INVALID)
        // 不在这里显示错误消息，由路由守卫统一处理
        const userStore = useUserStore()
        // 直接清除本地状态，不调用logout接口
        userStore.setToken('')
        userStore.setUserInfo(null)
        // 只有非token验证接口才跳转登录页并显示消息
        if (!response.config.url?.includes('/login/token')) {
          message.error(t('error.tokenExpired'))
          window.location.href = '/login'
        }
      } else {
        // 其他错误
        message.error(res.msg || t('error.requestFailed'))
      }
      return Promise.reject(new Error(res.msg || 'Error'))
    }
    
    return res
  },
  (error) => {
    console.error('Response error:', error)
    
    if (error.response) {
      // 服务器返回了错误状态码
      const status = error.response.status
      const code = error.response.data?.code
      
      // 特殊处理1112错误码
      if (code === 1112) {
        const userStore = useUserStore()
        userStore.setToken('')
        userStore.setUserInfo(null)
        // 只有非token验证接口才跳转登录页并显示消息
        if (!error.config?.url?.includes('/login/token')) {
          message.error(t('error.tokenExpired'))
          window.location.href = '/login'
        }
        return Promise.reject(error)
      }
      
      switch (status) {
        case 401:
          message.error(t('error.unauthorized'))
          const userStore = useUserStore()
          // 直接清除本地状态，不调用logout接口
          userStore.setToken('')
          userStore.setUserInfo(null)
          window.location.href = '/login'
          break
        case 403:
          message.error(t('error.forbidden'))
          break
        case 404:
          message.error(t('error.notFound'))
          break
        case 500:
          message.error(t('error.serverError'))
          break
        default:
          message.error(error.response.data?.msg || t('error.requestFailed'))
      }
    } else if (error.request) {
      // 请求已发送但没有收到响应
      message.error(t('error.networkError'))
    } else {
      // 其他错误
      message.error(t('error.requestFailed'))
    }
    
    return Promise.reject(error)
  }
)

/**
 * 验证token是否有效
 * @returns Promise<boolean> - token是否有效
 */
export const verifyToken = async (): Promise<boolean> => {
  try {
    const response = await request.get('/login/token')
    // 响应拦截器返回的是res(即response.data)，code为0表示token有效
    return (response as any).code === 0
  } catch (error: any) {
    // 当code为1112或其他错误时，响应拦截器会抛出异常
    // 都认为token无效
    return false
  }
}

/**
 * 处理token验证失败的情况
 * @param router - Vue Router实例
 */
export const handleTokenInvalid = (router: Router) => {
  const userStore = useUserStore()
  // 清除本地状态
  userStore.setToken('')
  userStore.setUserInfo(null)
  // 跳转到登录页
  router.push('/login')
  message.warning(t('error.tokenExpired'))
}

export default request
