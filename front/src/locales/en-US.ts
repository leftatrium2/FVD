export default {
  common: {
    save: 'Save',
    cancel: 'Cancel',
    confirm: 'Confirm',
    delete: 'Delete',
    edit: 'Edit',
    add: 'Add',
    search: 'Search',
    reset: 'Reset',
    refresh: 'Refresh',
    export: 'Export',
    import: 'Import',
    loading: 'Loading...',
    success: 'Success',
    error: 'Error',
    warning: 'Warning',
    info: 'Info',
    items: '',
    copyright: "Copyright © 2025 FVD Team. All rights reserved."
  },
  menu: {
    home: 'My Theater',
    download: 'Download Management',
    crawler: 'Crawler Management',
    addSingleTask: 'Add Single Task',
    addBatchTask: 'Add Batch Task',
    addScheduledTask: 'Add Scheduled Task',
    settings: 'Settings',
    general: 'Download Settings',
    video: 'Video Settings',
    proxy: 'Proxy Settings',
    logs: 'Logs',
    upgrade: 'Upgrade to Pro',
    about: 'About'
  },
  login: {
    title: 'FVD',
    subtitle: 'Video Downloader',
    username: 'Username',
    password: 'Password',
    rememberMe: 'Remember me',
    forgotPassword: 'Forgot password?',
    loginButton: 'Login',
    noAccount: 'Don\'t have an account?',
    register: 'Sign up now',
    usernamePlaceholder: 'Enter username',
    passwordPlaceholder: 'Enter password',
    usernameRequired: 'Please enter username!',
    passwordRequired: 'Please enter password!',
    loginSuccess: 'Login successful!',
    loginFailed: 'Login failed, please try again',
    usernameOrPasswordError: 'Incorrect username or password',
    networkError: 'Network connection failed, please check your network settings'
  },
  home: {
    title: 'Home',
    libraryType: 'All Libraries',
    searchPlaceholder: 'Keywords',
    confirm: 'Confirm',
    viewMode: 'View',
    simpleView: 'Simple View',
    complexView: 'Complex View',
    complexList: 'Complex View',
    simpleList: 'Simple View',
    table: {
      materialId: 'Material ID',
      title: 'Title',
      description: 'Description',
      author: 'Author',
      video: 'Video',
      audio: 'Audio',
      subtitle: 'Subtitle',
      library: 'Library',
      operation: 'Operation',
      delete: 'Delete',
      watchContinue: 'Subtitle Link',
      platform: 'youtube'
    }
  },
  download: {
    title: 'Download Manager',
    newTask: 'New Task',
    startAll: 'Start All',
    pauseAll: 'Pause All',
    clearCompleted: 'Clear Completed',
    tabs: {
      all: 'All',
      downloading: 'Downloading',
      completed: 'Completed',
      failed: 'Failed'
    },
    actions: {
      start: 'Start',
      pause: 'Pause',
      retry: 'Retry',
      open: 'Open',
      delete: 'Delete'
    },
    confirmDelete: 'Confirm Delete',
    confirmDeleteContent: 'Are you sure to delete task "{title}"?',
    confirmClear: 'Confirm Clear',
    confirmClearContent: 'Are you sure to clear all completed tasks?',
    allStarted: 'All tasks started',
    allPaused: 'All tasks paused',
    cleared: 'All completed tasks cleared',
    taskStarted: 'Task started',
    taskPaused: 'Task paused',
    taskRetried: 'Task retried',
    taskDeleted: 'Task deleted'
  },
  addSingleTask: {
    title: 'Add Download Task',
    linkLabel: 'Link:',
    url: 'Video URL',
    urlPlaceholder: 'https://www.youtube.com/@harryjaggerdtravel',
    urlRequired: 'Please enter video URL!',
    detectButton: 'Download',
    detectSuccess: 'add download task successful',
    detectFailed: 'Download failed',
    downloadButton: 'Download',
    downloadStarted: 'Download started',
    videoTitle: 'Video Title',
    titlePlaceholder: 'Optional, auto-fetch if empty',
    quality: 'Quality',
    savePath: 'Save Path',
    savePathPlaceholder: 'Select save location',
    browse: 'Browse',
    autoStart: 'Start download immediately after adding',
    parsePlaylist: 'Parse playlist',
    addButton: 'Add Task',
    addSuccess: 'Task added successfully!',
    addFailed: 'Failed to add task',
    qualities: {
      best: 'Best Quality',
      '1080p': '1080P',
      '720p': '720P',
      '480p': '480P',
      '360p': '360P'
    }
  },
  addBatchTask: {
    title: 'Batch Add Tasks',
    urls: 'Batch Video URLs',
    urlsPlaceholder: 'One link per line, support batch adding\nExample:\nhttps://example.com/video1.mp4\nhttps://example.com/video2.mp4\nhttps://example.com/video3.mp4',
    urlsRequired: 'Please enter video URLs!',
    concurrent: 'Concurrent Downloads',
    autoRename: 'Auto-rename duplicate files',
    detectedLinks: 'Detected {count} links',
    batchAdd: 'Batch Add ({count})',
    addSuccess: 'Successfully added {count} tasks!',
    selectFolder: 'Please select save folder'
  },
  settings: {
    general: {
      title: 'Download Settings',
      downloadSettings: 'Download Settings',
      defaultSavePath: 'Default Save Path',
      defaultQuality: 'Default Quality',
      maxConcurrent: 'Max Concurrent Downloads',
      speedLimit: 'Speed Limit (MB/s)',
      speedLimitPlaceholder: '0 means no limit',
      autoStart: 'Auto-start download after adding task',
      autoRetry: 'Auto-retry on download failure',
      deleteAfterComplete: 'Delete source task after completion',
      appSettings: 'Application Settings',
      language: 'Language',
      theme: 'Theme',
      themeLight: 'Light',
      themeDark: 'Dark',
      themeAuto: 'Auto',
      autoUpdate: 'Auto-check for updates',
      startOnBoot: 'Start on boot',
      minimizeToTray: 'Minimize to tray on close',
      saveButton: 'Save Settings',
      restoreDefaults: 'Restore Defaults',
      saveSuccess: 'Settings saved successfully!',
      restored: 'Default settings restored'
    },
    video: {
      title: 'Video Settings'
    },
    proxy: {
      title: 'Proxy Settings'
    },
    logs: {
      title: 'Logs',
      all: 'All',
      info: 'Info',
      warning: 'Warning',
      error: 'Error',
      refresh: 'Refresh',
      clear: 'Clear Logs',
      export: 'Export Logs',
      searchPlaceholder: 'Search log content...',
      totalLogs: 'Total {count} logs',
      confirmClear: 'Confirm Clear',
      confirmClearContent: 'Are you sure to clear all logs? This action cannot be undone.',
      cleared: 'Logs cleared',
      refreshed: 'Logs refreshed',
      exported: 'Logs exported'
    },
    upgrade: {
      title: 'Upgrade to Pro',
      subtitle: 'Unlock more powerful features and enhance download experience',
      features: {
        speed: {
          title: 'Lightning Speed',
          desc: 'Multi-threaded acceleration, 10x faster download speed'
        },
        cloud: {
          title: 'Cloud Storage',
          desc: '100GB cloud space, access anywhere anytime'
        },
        noAds: {
          title: 'Ad-Free',
          desc: 'Clean interface, focus on downloading'
        },
        batch: {
          title: 'Batch Download',
          desc: 'Support unlimited batch tasks'
        },
        schedule: {
          title: 'Scheduled Download',
          desc: 'Smart scheduling, save bandwidth'
        },
        support: {
          title: 'Priority Support',
          desc: '7x24 dedicated customer service'
        }
      },
      plans: {
        title: 'Choose Subscription Plan',
        monthly: {
          title: 'Monthly',
          price: '$4.99',
          period: '/month'
        },
        yearly: {
          title: 'Yearly',
          price: '$29.99',
          period: '/year',
          badge: 'Recommended',
          save: 'Save $29.89'
        },
        lifetime: {
          title: 'Lifetime',
          price: '$89.99'
        },
        subscribe: 'Subscribe Now',
        purchase: 'Purchase Now'
      },
      notes: {
        refund: '* All subscriptions support 7-day money-back guarantee',
        payment: '* Support Alipay, WeChat Pay, Credit Card and more'
      }
    },
    about: {
      title: 'FVD',
      subtitle: 'Video Downloader',
      version: 'Version',
      releaseDate: 'Release Date',
      developer: 'Developer',
      website: 'Website',
      support: 'Support',
      introduction: 'Introduction',
      introText1: 'FVD is a powerful video download tool that supports multiple video platforms and provides fast and stable download experience.',
      introText2: 'Using advanced multi-threaded download technology and intelligent resume capability, making your downloads faster and more stable.',
      features: 'Main Features',
      featureList: {
        platforms: 'Support multiple video platforms',
        speed: 'Multi-threaded high-speed download',
        resume: 'Intelligent resume capability',
        batch: 'Batch download management',
        quality: 'Custom download quality',
        ui: 'Clean and beautiful user interface'
      },
      checkUpdate: 'Check Update',
      github: 'Visit GitHub',
      docs: 'View Docs',
      checkingUpdate: 'Checking for updates...',
      latestVersion: 'You are using the latest version',
      copyright: 'Copyright © 2025 FVD Team. All rights reserved.',
      privacy: 'Privacy Policy',
      terms: 'Terms of Service',
      license: 'Open Source License'
    }
  },
  user: {
    profile: 'Profile',
    logout: 'Logout',
    logoutSuccess: 'Logout successful'
  },
  error: {
    tokenExpired: 'Login expired, please login again',
    unauthorized: 'Unauthorized, please login',
    forbidden: 'Access denied',
    notFound: 'Request address not found',
    serverError: 'Server internal error',
    requestFailed: 'Request failed',
    networkError: 'Network connection failed, please check network settings'
  }
}

