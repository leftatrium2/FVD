export default defineNuxtConfig({
  devtools: { enabled: true },
  
  modules: ['@nuxtjs/i18n'],
  
  i18n: {
    locales: [
      { code: 'zh', language: 'zh-CN', name: '中文', file: 'zh.json' },
      { code: 'en', language: 'en-US', name: 'English', file: 'en.json' }
    ],
    lazy: true,
    langDir: 'locales',
    defaultLocale: 'zh',
    strategy: 'no_prefix',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root'
    }
  },
  
  app: {
    head: {
      title: 'iVD - Internet Video Downloader',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Internet Video Downloader - 专业的视频下载工具' },
        { name: 'keywords', content: 'video downloader, 视频下载, iVD' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },
  
  css: ['~/assets/css/main.css'],
  
  compatibilityDate: '2024-11-22'
})
