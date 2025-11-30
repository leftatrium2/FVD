<template>
  <a-layout class="min-h-screen">
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible :width="250" class="!bg-white shadow-md">
      <div class="h-16 flex items-center justify-center border-b">
        <h1 class="text-xl font-bold text-blue-600" v-if="!collapsed">FVD</h1>
        <h1 class="text-xl font-bold text-blue-600" v-else>FV</h1>
      </div>
      <a-menu
        v-model:selectedKeys="selectedKeys"
        mode="inline"
        class="border-r-0"
        @click="handleMenuClick"
      >
        <template v-for="item in menuList" :key="item.url || item.c_name">
          <!-- 无子菜单项 -->
          <a-menu-item v-if="!item.sub" :key="item.url">
            <template #icon>
              <component :is="getMenuIcon(item.url)" />
            </template>
            <span>{{ currentLanguage === 'zh-CN' ? item.c_name : item.e_name }}</span>
          </a-menu-item>
          
          <!-- 有子菜单项 -->
          <a-sub-menu v-else :key="item.c_name">
            <template #icon>
              <component :is="getMenuIcon('settings')" />
            </template>
            <template #title>{{ currentLanguage === 'zh-CN' ? item.c_name : item.e_name }}</template>
            <a-menu-item v-for="subItem in item.sub" :key="subItem.url">
              {{ currentLanguage === 'zh-CN' ? subItem.c_name : subItem.e_name }}
            </a-menu-item>
          </a-sub-menu>
        </template>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header class="!bg-white !px-6 shadow-sm flex items-center justify-between">
        <div class="flex items-center">
          <MenuUnfoldOutlined
            v-if="collapsed"
            class="text-lg cursor-pointer hover:text-blue-600"
            @click="() => (collapsed = !collapsed)"
          />
          <MenuFoldOutlined
            v-else
            class="text-lg cursor-pointer hover:text-blue-600"
            @click="() => (collapsed = !collapsed)"
          />
          <span class="ml-4 text-lg font-medium">{{ pageTitle }}</span>
        </div>
        <div class="flex items-center gap-4">
          <a-dropdown>
            <a class="ant-dropdown-link flex items-center gap-2" @click.prevent>
              <GlobalOutlined />
              <span>{{ currentLanguage === 'zh-CN' ? '中文' : 'English' }}</span>
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
          <a-dropdown>
            <a class="ant-dropdown-link flex items-center gap-2" @click.prevent>
              <UserOutlined />
              <span>{{ $t('user.profile') }}</span>
            </a>
            <template #overlay>
              <a-menu>
                <a-menu-item key="profile">
                  <UserOutlined />
                  <span class="ml-2">{{ $t('user.profile') }}</span>
                </a-menu-item>
                <a-menu-divider />
                <a-menu-item key="logout" @click="handleLogout">
                  <LogoutOutlined />
                  <span class="ml-2">{{ $t('user.logout') }}</span>
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </div>
      </a-layout-header>
      <a-layout-content class="m-6 p-6 bg-white rounded-lg shadow-sm">
        <router-view />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store/user'
import { useI18n } from 'vue-i18n'
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  HomeOutlined,
  CloudDownloadOutlined,
  BugOutlined,
  PlusCircleOutlined,
  PlusSquareOutlined,
  ClockCircleOutlined,
  SettingOutlined,
  UserOutlined,
  LogoutOutlined,
  GlobalOutlined
} from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import request from '@/utils/request'

interface MenuItem {
  c_name: string
  e_name: string
  url?: string
  sub?: MenuItem[]
}

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()
const { t, locale } = useI18n()

const collapsed = ref(false)
const selectedKeys = ref<string[]>([route.path])
const currentLanguage = computed(() => locale.value)
const menuList = ref<MenuItem[]>([])

const pageTitle = computed(() => {
  return route.meta.title as string || '首页'
})

// 获取菜单图标
const getMenuIcon = (url: string | undefined) => {
  if (!url) return HomeOutlined
  
  const iconMap: Record<string, any> = {
    '/home': HomeOutlined,
    '/download': CloudDownloadOutlined,
    '/crawler': BugOutlined,
    '/add-single-task': PlusCircleOutlined,
    '/add-batch-task': PlusSquareOutlined,
    '/import-batch-single-task': PlusSquareOutlined,
    '/add-scheduled-task': ClockCircleOutlined,
    'settings': SettingOutlined
  }
  
  return iconMap[url] || HomeOutlined
}

// 获取菜单数据
const fetchMenuData = async () => {
  try {
    const response = await request.get('/menu/')
    
    if (response.code === 0) {
      menuList.value = response.data || []
    } else {
      menuList.value = []
    }
  } catch (error) {
    console.error('获取菜单失败:', error)
    // 静默失败，不显示错误提示
    menuList.value = []
  }
}

const handleMenuClick = ({ key }: { key: string }) => {
  selectedKeys.value = [key]
  router.push(key)
}

const handleLogout = async () => {
  try {
    await userStore.logout()
    message.success(t('user.logoutSuccess'))
    router.push('/login')
  } catch (error) {
    console.error('Logout failed:', error)
    // 即使退出失败，也清除本地状态并跳转到登录页
    message.success(t('user.logoutSuccess'))
    router.push('/login')
  }
}

const handleLanguageChange = ({ key }: { key: string }) => {
  locale.value = key
  localStorage.setItem('language', key)
  message.success(key === 'zh-CN' ? '切换到中文' : 'Switched to English')
}

// 监听路由变化
router.afterEach((to) => {
  selectedKeys.value = [to.path]
})

// 组件挂载时获取菜单数据
onMounted(() => {
  fetchMenuData()
})
</script>

<style scoped>
:deep(.ant-layout-sider-trigger) {
  background: #fff;
  color: #000;
}
</style>
