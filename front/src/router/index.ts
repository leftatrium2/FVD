import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Layout from '@/components/Layout.vue'
import { verifyToken, handleTokenInvalid } from '@/utils/request'
import { message } from 'ant-design-vue'
import i18n from '@/locales'

/**
 * 获取国际化文本
 * @param key - 翻译key
 * @returns 翻译后的文本
 */
const t = (key: string): string => {
  return i18n.global.t(key)
}

const routes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { title: '登录' }
  },
  {
    path: '/',
    component: Layout,
    redirect: '/home',
    children: [
      {
        path: '/home',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: { title: '首页', icon: 'HomeOutlined' }
      },
      {
        path: '/download',
        name: 'Download',
        component: () => import('@/views/Download.vue'),
        meta: { title: '下载', icon: 'CloudDownloadOutlined' }
      },
      {
        path: '/crawler',
        name: 'Crawler',
        component: () => import('@/views/Crawler.vue'),
        meta: { title: '爬虫管理', icon: 'BugOutlined' }
      },
      {
        path: '/add-single-task',
        name: 'AddSingleTask',
        component: () => import('@/views/AddSingleTask.vue'),
        meta: { title: '添加单次任务', icon: 'PlusCircleOutlined' }
      },
      {
        path: '/add-batch-task',
        name: 'AddBatchTask',
        component: () => import('@/views/AddBatchTask.vue'),
        meta: { title: '添加批量任务', icon: 'PlusCircleOutlined' }
      },
      {
        path: '/add-scheduled-task',
        name: 'AddScheduledTask',
        component: () => import('@/views/AddScheduledTask.vue'),
        meta: { title: '添加定时任务', icon: 'ClockCircleOutlined' }
      },
      {
        path: '/settings',
        name: 'Settings',
        redirect: '/settings/general',
        meta: { title: '设置', icon: 'SettingOutlined' },
        children: [
          {
            path: '/settings/general',
            name: 'SettingsGeneral',
            component: () => import('@/views/settings/General.vue'),
            meta: { title: '下载设置' }
          },
          {
            path: '/settings/video',
            name: 'SettingsVideo',
            component: () => import('@/views/settings/Video.vue'),
            meta: { title: '视频设置' }
          },
          {
            path: '/settings/proxy',
            name: 'SettingsProxy',
            component: () => import('@/views/settings/Proxy.vue'),
            meta: { title: '代理设置' }
          },
          {
            path: '/settings/logs',
            name: 'SettingsLogs',
            component: () => import('@/views/settings/Logs.vue'),
            meta: { title: '日志查看' }
          },
          {
            path: '/settings/upgrade',
            name: 'SettingsUpgrade',
            component: () => import('@/views/settings/Upgrade.vue'),
            meta: { title: '升级到专业版' }
          },
          {
            path: '/settings/about',
            name: 'SettingsAbout',
            component: () => import('@/views/settings/About.vue'),
            meta: { title: '关于' }
          }
        ]
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 全局前置守卫 - 验证token
router.beforeEach(async (to, from, next) => {
  // 如果是去登录页，直接放行
  if (to.path === '/login') {
    next()
    return
  }

  // 验证token
  const isValid = await verifyToken()
  
  if (isValid) {
    // token有效，放行
    next()
  } else {
    // token无效，跳转到登录页
    handleTokenInvalid(router)
    next(false) // 取消当前导航
  }
})

export default router
