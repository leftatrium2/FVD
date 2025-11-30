export default {
  common: {
    save: '保存',
    cancel: '取消',
    confirm: '确认',
    delete: '删除',
    edit: '编辑',
    add: '添加',
    search: '搜索',
    reset: '重置',
    refresh: '刷新',
    export: '导出',
    import: '导入',
    loading: '加载中...',
    success: '成功',
    error: '错误',
    warning: '警告',
    info: '信息',
    items: '个',
    copyright: "Copyright © 2025 FVD 公司. All rights reserved."
  },
  menu: {
    home: '我的影院',
    download: '下载管理',
    crawler: '爬虫管理',
    addSingleTask: '添加单次任务',
    addBatchTask: '添加批量任务',
    addScheduledTask: '添加定时任务',
    settings: '设置',
    general: '下载设置',
    video: '视频设置',
    proxy: '代理设置',
    logs: '日志查看',
    upgrade: '升级到专业版',
    about: '关于'
  },
  login: {
    title: 'FVD',
    subtitle: '视频下载工具',
    username: '用户名',
    password: '密码',
    rememberMe: '记住我',
    forgotPassword: '忘记密码?',
    loginButton: '登录',
    noAccount: '还没有账号?',
    register: '立即注册',
    usernamePlaceholder: '请输入用户名',
    passwordPlaceholder: '请输入密码',
    usernameRequired: '请输入用户名!',
    passwordRequired: '请输入密码!',
    loginSuccess: '登录成功!',
    loginFailed: '登录失败，请重试',
    usernameOrPasswordError: '用户名或密码错误',
    networkError: '网络连接失败，请检查网络设置'
  },
  home: {
    title: '首页',
    libraryType: '全部素材库',
    searchPlaceholder: '关键词',
    confirm: '确认',
    viewMode: '界面',
    simpleView: '简单界面',
    complexView: '复杂界面',
    complexList: '复杂界面',
    simpleList: '简单界面',
    table: {
      materialId: '素材id',
      title: '标题',
      description: '描述',
      author: '作者',
      video: '视频',
      audio: '音频',
      subtitle: '字幕',
      library: '所属素材库',
      operation: '操作',
      delete: '删除',
      watchContinue: '字幕连接',
      platform: 'youtube'
    }
  },
  download: {
    title: '下载管理',
    newTask: '新建任务',
    startAll: '全部开始',
    pauseAll: '全部暂停',
    clearCompleted: '清除已完成',
    tabs: {
      all: '全部',
      downloading: '下载中',
      completed: '已完成',
      failed: '失败'
    },
    actions: {
      start: '开始',
      pause: '暂停',
      retry: '重试',
      open: '打开',
      delete: '删除'
    },
    confirmDelete: '确认删除',
    confirmDeleteContent: '确定要删除任务"{title}"吗？',
    confirmClear: '确认清除',
    confirmClearContent: '确定要清除所有已完成的任务吗？',
    allStarted: '已开始全部任务',
    allPaused: '已暂停全部任务',
    cleared: '已清除所有已完成任务',
    taskStarted: '任务已开始',
    taskPaused: '任务已暂停',
    taskRetried: '任务已重试',
    taskDeleted: '任务已删除'
  },
  addSingleTask: {
    title: '添加下载任务',
    linkLabel: '链接：',
    linkTip: '添加多个视频链接，使用换行分割。最多支持20个链接，如果需要批量导入功能，请升级到专业版',
    url: '视频链接',
    urlPlaceholder: 'https://www.youtube.com/@harryjaggerdtravel',
    urlRequired: '请输入视频链接!',
    detectButton: '下载',
    detectSuccess: '添加下载任务成功',
    detectFailed: '下载失败',
    downloadButton: '下载',
    downloadStarted: '开始下载',
    videoTitle: '视频标题',
    titlePlaceholder: '选填，留空则自动获取',
    quality: '下载质量',
    savePath: '保存路径',
    savePathPlaceholder: '选择保存位置',
    browse: '浏览',
    autoStart: '添加后立即开始下载',
    parsePlaylist: '解析播放列表',
    addButton: '添加任务',
    addSuccess: '任务添加成功!',
    addFailed: '添加任务失败',
    qualities: {
      best: '最佳质量',
      '1080p': '1080P',
      '720p': '720P',
      '480p': '480P',
      '360p': '360P'
    }
  },
  addBatchTask: {
    title: '批量添加任务',
    urls: '批量视频链接',
    urlsPlaceholder: '每行一个链接，支持批量添加\n例如：\nhttps://example.com/video1.mp4\nhttps://example.com/video2.mp4\nhttps://example.com/video3.mp4',
    urlsRequired: '请输入视频链接!',
    concurrent: '并发下载数',
    autoRename: '自动重命名重复文件',
    detectedLinks: '检测到 {count} 个链接',
    batchAdd: '批量添加 ({count})',
    addSuccess: '成功添加 {count} 个任务!',
    selectFolder: '请选择保存文件夹'
  },
  settings: {
    general: {
      title: '下载设置',
      downloadSettings: '下载设置',
      defaultSavePath: '默认保存路径',
      defaultQuality: '默认下载质量',
      maxConcurrent: '最大并发下载数',
      speedLimit: '下载速度限制 (MB/s)',
      speedLimitPlaceholder: '0表示不限速',
      autoStart: '添加任务后自动开始下载',
      autoRetry: '下载失败后自动重试',
      deleteAfterComplete: '下载完成后删除源任务',
      appSettings: '应用设置',
      language: '界面语言',
      theme: '主题',
      themeLight: '浅色',
      themeDark: '深色',
      themeAuto: '跟随系统',
      autoUpdate: '自动检查更新',
      startOnBoot: '开机自动启动',
      minimizeToTray: '关闭时最小化到托盘',
      saveButton: '保存设置',
      restoreDefaults: '恢复默认',
      saveSuccess: '设置保存成功!',
      restored: '已恢复默认设置'
    },
    video: {
      title: '视频设置'
    },
    proxy: {
      title: '代理设置'
    },
    logs: {
      title: '日志查看',
      all: '全部',
      info: '信息',
      warning: '警告',
      error: '错误',
      refresh: '刷新',
      clear: '清空日志',
      export: '导出日志',
      searchPlaceholder: '搜索日志内容...',
      totalLogs: '共 {count} 条日志',
      confirmClear: '确认清空',
      confirmClearContent: '确定要清空所有日志吗？此操作不可恢复。',
      cleared: '日志已清空',
      refreshed: '日志已刷新',
      exported: '日志已导出'
    },
    upgrade: {
      title: '升级到专业版',
      subtitle: '解锁更多强大功能，提升下载体验',
      features: {
        speed: {
          title: '极速下载',
          desc: '多线程加速，下载速度提升10倍'
        },
        cloud: {
          title: '云端存储',
          desc: '100GB云端空间，随时随地访问'
        },
        noAds: {
          title: '无广告体验',
          desc: '纯净界面，专注下载'
        },
        batch: {
          title: '批量下载',
          desc: '支持无限量批量任务'
        },
        schedule: {
          title: '定时下载',
          desc: '智能调度，节省带宽'
        },
        support: {
          title: '优先支持',
          desc: '7x24小时专属客服'
        }
      },
      plans: {
        title: '选择订阅计划',
        monthly: {
          title: '月度订阅',
          price: '¥29',
          period: '/月'
        },
        yearly: {
          title: '年度订阅',
          price: '¥199',
          period: '/年',
          badge: '推荐',
          save: '节省¥149'
        },
        lifetime: {
          title: '终身授权',
          price: '¥599'
        },
        subscribe: '立即订阅',
        purchase: '立即购买'
      },
      notes: {
        refund: '* 所有订阅均支持7天无理由退款',
        payment: '* 支持支付宝、微信、银行卡等多种支付方式'
      }
    },
    about: {
      title: 'FVD',
      subtitle: '视频下载工具',
      version: '版本号',
      releaseDate: '发布日期',
      developer: '开发者',
      website: '官网',
      support: '技术支持',
      introduction: '产品介绍',
      introText1: 'FVD是一款功能强大的视频下载工具，支持多种视频平台的下载，提供极速、稳定的下载体验。',
      introText2: '采用先进的多线程下载技术，智能断点续传，让您的下载更快更稳定。',
      features: '主要功能',
      featureList: {
        platforms: '支持多种视频平台下载',
        speed: '多线程极速下载',
        resume: '智能断点续传',
        batch: '批量下载管理',
        quality: '自定义下载质量',
        ui: '简洁美观的用户界面'
      },
      checkUpdate: '检查更新',
      github: '访问GitHub',
      docs: '查看文档',
      checkingUpdate: '正在检查更新...',
      latestVersion: '当前已是最新版本',
      copyright: 'Copyright © 2025 FVD Team. All rights reserved.',
      privacy: '隐私政策',
      terms: '使用条款',
      license: '开源许可'
    }
  },
  user: {
    profile: '个人中心',
    logout: '退出登录',
    logoutSuccess: '退出登录成功'
  },
  error: {
    tokenExpired: '登录已过期，请重新登录',
    unauthorized: '未授权，请登录',
    forbidden: '拒绝访问',
    notFound: '请求地址不存在',
    serverError: '服务器内部错误',
    requestFailed: '请求失败',
    networkError: '网络连接失败，请检查网络设置'
  }
}

