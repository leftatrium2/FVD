<template>
  <div>
    <a-card :title="$t('settings.logs.title')" :bordered="false">
      <template #extra>
        <a-space>
          <a-select v-model:value="logLevel" style="width: 120px">
            <a-select-option value="all">{{ $t('settings.logs.all') }}</a-select-option>
            <a-select-option value="info">{{ $t('settings.logs.info') }}</a-select-option>
            <a-select-option value="warning">{{ $t('settings.logs.warning') }}</a-select-option>
            <a-select-option value="error">{{ $t('settings.logs.error') }}</a-select-option>
          </a-select>
          <a-button @click="refreshLogs">
            <ReloadOutlined />
            {{ $t('settings.logs.refresh') }}
          </a-button>
          <a-button @click="clearLogs" danger>
            <DeleteOutlined />
            {{ $t('settings.logs.clear') }}
          </a-button>
          <a-button @click="exportLogs">
            <ExportOutlined />
            {{ $t('settings.logs.export') }}
          </a-button>
        </a-space>
      </template>

      <div class="mb-4">
        <a-input-search
          v-model:value="searchText"
          :placeholder="$t('settings.logs.searchPlaceholder')"
          style="width: 300px"
          @search="handleSearch"
        />
      </div>

      <div class="log-container bg-gray-900 text-gray-100 p-4 rounded-lg font-mono text-sm overflow-auto" style="height: 500px;">
        <div v-for="log in filteredLogs" :key="log.id" class="log-item mb-2">
          <span :class="getLogLevelClass(log.level)" class="font-bold">[{{ log.level }}]</span>
          <span class="text-gray-400 ml-2">{{ log.timestamp }}</span>
          <span class="ml-2">{{ log.message }}</span>
        </div>
      </div>

      <div class="mt-4 text-gray-500 text-sm">
        {{ $t('settings.logs.totalLogs', { count: logs.length }) }}
      </div>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { ReloadOutlined, DeleteOutlined, ExportOutlined } from '@ant-design/icons-vue'
import { message, Modal } from 'ant-design-vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'

const { t } = useI18n()

interface LogItem {
  id: number
  level: 'INFO' | 'WARNING' | 'ERROR'
  timestamp: string
  message: string
}

const logLevel = ref('all')
const searchText = ref('')

const logs = ref<LogItem[]>([
  { id: 1, level: 'INFO', timestamp: '2025-11-22 10:00:00', message: '应用程序启动成功' },
  { id: 2, level: 'INFO', timestamp: '2025-11-22 10:05:23', message: '开始下载任务: example_video.mp4' },
  { id: 3, level: 'INFO', timestamp: '2025-11-22 10:10:45', message: '任务下载完成: example_video.mp4' },
  { id: 4, level: 'WARNING', timestamp: '2025-11-22 10:15:12', message: '网络连接不稳定，正在重试...' },
  { id: 5, level: 'ERROR', timestamp: '2025-11-22 10:20:33', message: '下载失败: network_error.mp4 - 连接超时' },
  { id: 6, level: 'INFO', timestamp: '2025-11-22 10:25:56', message: '自动重试下载: network_error.mp4' },
  { id: 7, level: 'INFO', timestamp: '2025-11-22 10:30:18', message: '任务下载完成: network_error.mp4' },
  { id: 8, level: 'INFO', timestamp: '2025-11-22 10:35:42', message: '检查更新: 当前版本 v1.0.0' },
  { id: 9, level: 'WARNING', timestamp: '2025-11-22 10:40:05', message: '磁盘空间不足，剩余 500MB' },
  { id: 10, level: 'INFO', timestamp: '2025-11-22 10:45:28', message: '用户设置已保存' }
])

const filteredLogs = computed(() => {
  let result = logs.value

  // 按日志级别过滤
  if (logLevel.value !== 'all') {
    result = result.filter(log => log.level.toLowerCase() === logLevel.value.toLowerCase())
  }

  // 按搜索文本过滤
  if (searchText.value) {
    result = result.filter(log => 
      log.message.toLowerCase().includes(searchText.value.toLowerCase())
    )
  }

  return result
})

const getLogLevelClass = (level: string) => {
  const classes: Record<string, string> = {
    INFO: 'text-blue-400',
    WARNING: 'text-yellow-400',
    ERROR: 'text-red-400'
  }
  return classes[level] || 'text-gray-400'
}

const refreshLogs = () => {
  message.success(t('settings.logs.refreshed'))
}

const clearLogs = () => {
  Modal.confirm({
    title: t('settings.logs.confirmClear'),
    content: t('settings.logs.confirmClearContent'),
    okText: t('common.confirm'),
    cancelText: t('common.cancel'),
    onOk: () => {
      logs.value = []
      message.success(t('settings.logs.cleared'))
    }
  })
}

const exportLogs = () => {
  const logContent = logs.value
    .map(log => `[${log.level}] ${log.timestamp} - ${log.message}`)
    .join('\n')
  
  const blob = new Blob([logContent], { type: 'text/plain' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `ivd-logs-${new Date().getTime()}.txt`
  a.click()
  URL.revokeObjectURL(url)
  
  message.success(t('settings.logs.exported'))
}

const handleSearch = () => {
  // 搜索逻辑已在computed中实现
}
</script>

<style scoped>
.log-container::-webkit-scrollbar {
  width: 8px;
}

.log-container::-webkit-scrollbar-track {
  background: #1f2937;
}

.log-container::-webkit-scrollbar-thumb {
  background: #4b5563;
  border-radius: 4px;
}

.log-container::-webkit-scrollbar-thumb:hover {
  background: #6b7280;
}
</style>
