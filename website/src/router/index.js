import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import News from '../views/News.vue'
import Features from '../views/Features.vue'
import Download from '../views/Download.vue'
import Support from '../views/Support.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'iVD - Internet Video Downloader',
      description: 'iVD是一款功能强大的视频下载工具，支持多平台视频下载'
    }
  },
  {
    path: '/news',
    name: 'News',
    component: News,
    meta: {
      title: '新闻 - iVD',
      description: 'iVD最新新闻和更新信息'
    }
  },
  {
    path: '/features',
    name: 'Features',
    component: Features,
    meta: {
      title: '特性 - iVD',
      description: 'iVD视频下载工具的强大功能特性'
    }
  },
  {
    path: '/download',
    name: 'Download',
    component: Download,
    meta: {
      title: '下载 - iVD',
      description: '下载iVD视频下载工具'
    }
  },
  {
    path: '/support',
    name: 'Support',
    component: Support,
    meta: {
      title: '支持 - iVD',
      description: 'iVD技术支持和帮助中心'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫 - 更新页面标题和meta标签
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  if (to.meta.description) {
    let descriptionMeta = document.querySelector('meta[name="description"]')
    if (descriptionMeta) {
      descriptionMeta.setAttribute('content', to.meta.description)
    }
  }
  next()
})

export default router
