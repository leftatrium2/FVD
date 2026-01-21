import { createI18n } from 'vue-i18n'

const messages = {
  zh: {
    menu: {
      home: '我的影院',
      download: '下载管理',
      addSingleTask: '添加单次任务',
      addScheduledTask: '添加定时任务',
    },
    common: {
      language: '语言',
      chinese: '中文',
      english: '英文',
    },
    home: {
      title: '我的影院',
      welcome: '欢迎使用 Full Video Downloader',
    },
    download: {
      title: '下载管理',
    },
    addTask: {
      singleTitle: '添加单次任务',
      scheduledTitle: '添加定时任务',
    }
  },
  en: {
    menu: {
      home: 'My Cinema',
      download: 'Downloads',
      addSingleTask: 'Add Single Task',
      addScheduledTask: 'Add Scheduled Task',
    },
    common: {
      language: 'Language',
      chinese: 'Chinese',
      english: 'English',
    },
    home: {
      title: 'My Cinema',
      welcome: 'Welcome to Full Video Downloader',
    },
    download: {
      title: 'Downloads',
    },
    addTask: {
      singleTitle: 'Add Single Task',
      scheduledTitle: 'Add Scheduled Task',
    }
  },
}

const i18n = createI18n({
  legacy: false,
  locale: 'zh',
  fallbackLocale: 'en',
  messages,
})

export default i18n
