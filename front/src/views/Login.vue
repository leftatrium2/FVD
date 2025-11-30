<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-blue-50 to-indigo-100">
    <!-- 语言选择器 -->
    <div class="absolute top-4 right-4">
      <a-dropdown>
        <a class="ant-dropdown-link flex items-center gap-2 bg-white px-3 py-2 rounded-lg shadow hover:shadow-md transition-shadow" @click.prevent>
          <GlobalOutlined />
          <span>{{ currentLanguage === 'zh-CN' ? '中文' : 'English' }}</span>
          <DownOutlined style="font-size: 12px" />
        </a>
        <template #overlay>
          <a-menu @click="handleLanguageChange">
            <a-menu-item key="zh-CN">
              <span>中文</span>
            </a-menu-item>
            <a-menu-item key="en-US">
              <span>English</span>
            </a-menu-item>
          </a-menu>
        </template>
      </a-dropdown>
    </div>
    
    <div class="flex-1 flex items-center justify-center py-12">
      <div class="w-full max-w-md">
        <a-card class="shadow-xl rounded-xl">
        <div class="text-center mb-8">
          <h1 class="text-4xl font-bold text-blue-600 mb-2">{{ $t('login.title') }}</h1>
          <p class="text-gray-500">{{ $t('login.subtitle') }}</p>
        </div>
        <a-form
          :model="formState"
          name="login"
          @finish="onFinish"
          autocomplete="off"
          layout="vertical"
        >
          <a-form-item
            :label="$t('login.username')"
            name="username"
            :rules="[{ required: true, message: $t('login.usernameRequired') }]"
          >
            <a-input v-model:value="formState.username" size="large" :placeholder="$t('login.usernamePlaceholder')">
              <template #prefix>
                <UserOutlined class="text-gray-400" />
              </template>
            </a-input>
          </a-form-item>

          <a-form-item
            :label="$t('login.password')"
            name="password"
            :rules="[{ required: true, message: $t('login.passwordRequired') }]"
          >
            <a-input-password v-model:value="formState.password" size="large" :placeholder="$t('login.passwordPlaceholder')">
              <template #prefix>
                <LockOutlined class="text-gray-400" />
              </template>
            </a-input-password>
          </a-form-item>

          <a-form-item>
            <div class="flex items-center justify-between">
              <a-checkbox v-model:checked="formState.remember">{{ $t('login.rememberMe') }}</a-checkbox>
              <a class="text-blue-600 hover:text-blue-700">{{ $t('login.forgotPassword') }}</a>
            </div>
          </a-form-item>

          <a-form-item>
            <a-button type="primary" html-type="submit" size="large" block :loading="loading">
              {{ $t('login.loginButton') }}
            </a-button>
          </a-form-item>
        </a-form>
        <div class="text-center text-gray-500 text-sm mt-4">
          {{ $t('login.noAccount') }} <a class="text-blue-600 hover:text-blue-700">{{ $t('login.register') }}</a>
        </div>
      </a-card>
      </div>
    </div>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/store/user'
import { UserOutlined, LockOutlined, GlobalOutlined, DownOutlined } from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'
import request from '@/utils/request'

const router = useRouter()
const userStore = useUserStore()
const { t, locale } = useI18n()

const currentLanguage = computed(() => locale.value)

const formState = reactive({
  username: '',
  password: '',
  remember: true
})

const loading = ref(false)

const handleLanguageChange = ({ key }: { key: string }) => {
  locale.value = key
  localStorage.setItem('language', key)
  message.success(key === 'zh-CN' ? '语言已切换为中文' : 'Language switched to English')
}

const onFinish = async (values: any) => {
  loading.value = true
  try {
    // 调用后台登录接口
    const response = await request.post('/login/', {
      username: values.username,
      password: values.password
    })
    
    // 登录成功（request拦截器已处理code !== 0的情况）
    const { token, username, nickname, avatar, roles, permissions, expires } = response.data
    
    // 保存token
    userStore.setToken(token)
    
    // 保存用户信息
    userStore.setUserInfo({
      username: username,
      name: nickname || username,
      avatar: avatar,
      roles: roles,
      permissions: permissions,
      expires: expires
    })
    
    message.success(t('login.loginSuccess'))
    
    // 跳转到首页
    router.push('/home')
  } catch (error: any) {
    console.error('Login error:', error)
    
    // 错误处理已在request拦截器中统一处理
    // 这里只需要处理特定的登录错误
    if (error.response?.data?.code === 1105) {
      message.error(t('login.usernameOrPasswordError'))
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
</style>
