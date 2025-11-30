import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import router from './router'
import App from './App.vue'
import './style.css'

// 导入语言包
import zh from './locales/zh.json'
import en from './locales/en.json'

// 配置国际化
const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('language') || 'zh',
  fallbackLocale: 'zh',
  messages: {
    zh,
    en
  }
})

const app = createApp(App)
app.use(router)
app.use(i18n)
app.mount('#app')
