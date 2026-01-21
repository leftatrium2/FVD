import { createRouter, createWebHashHistory } from 'vue-router'
import MainLayout from '../layout/MainLayout.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      component: MainLayout,
      redirect: '/home',
      children: [
        {
          path: 'home',
          name: 'Home',
          component: () => import('../views/Home.vue'),
        },
        {
          path: 'download',
          name: 'Download',
          component: () => import('../views/Download.vue'),
        },
        {
          path: 'add-single-task',
          name: 'AddSingleTask',
          component: () => import('../views/AddSingleTask.vue'),
        },
        {
          path: 'add-scheduled-task',
          name: 'AddScheduledTask',
          component: () => import('../views/AddScheduledTask.vue'),
        },
      ],
    },
  ],
})

export default router
