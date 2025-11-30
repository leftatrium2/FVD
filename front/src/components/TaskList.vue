<template>
  <a-list :data-source="tasks" :loading="false">
    <template #renderItem="{ item }">
      <a-list-item>
        <a-list-item-meta>
          <template #title>
            <div class="flex items-center justify-between">
              <span class="font-medium">{{ item.title }}</span>
              <a-tag :color="getStatusColor(item.status)">
                {{ getStatusText(item.status) }}
              </a-tag>
            </div>
          </template>
          <template #description>
            <div class="space-y-2">
              <div class="text-sm text-gray-500 truncate">{{ item.url }}</div>
              <div v-if="item.status === 'downloading' || item.status === 'paused'">
                <a-progress :percent="item.progress" :status="item.status === 'paused' ? 'exception' : 'active'" />
                <div class="flex items-center justify-between text-xs text-gray-500 mt-1">
                  <span>{{ item.speed || '计算中...' }}</span>
                  <span>{{ item.size || '未知大小' }}</span>
                </div>
              </div>
              <div v-else-if="item.status === 'completed'" class="text-sm text-gray-500">
                文件大小: {{ item.size || '未知' }}
              </div>
            </div>
          </template>
        </a-list-item-meta>
        <template #actions>
          <a-space>
            <a-button
              v-if="item.status === 'paused' || item.status === 'waiting'"
              type="link"
              size="small"
              @click="emit('action', { action: 'start', taskId: item.id })"
            >
              <PlayCircleOutlined />
              {{ $t('download.actions.start') }}
            </a-button>
            <a-button
              v-if="item.status === 'downloading'"
              type="link"
              size="small"
              @click="emit('action', { action: 'pause', taskId: item.id })"
            >
              <PauseCircleOutlined />
              {{ $t('download.actions.pause') }}
            </a-button>
            <a-button
              v-if="item.status === 'failed'"
              type="link"
              size="small"
              @click="emit('action', { action: 'retry', taskId: item.id })"
            >
              <ReloadOutlined />
              {{ $t('download.actions.retry') }}
            </a-button>
            <a-button
              v-if="item.status === 'completed'"
              type="link"
              size="small"
            >
              <FolderOpenOutlined />
              {{ $t('download.actions.open') }}
            </a-button>
            <a-button
              type="link"
              size="small"
              danger
              @click="emit('action', { action: 'delete', taskId: item.id })"
            >
              <DeleteOutlined />
              {{ $t('download.actions.delete') }}
            </a-button>
          </a-space>
        </template>
      </a-list-item>
    </template>
  </a-list>
</template>

<script setup lang="ts">
import { PropType } from 'vue'
import { DownloadTask } from '@/store/download'
import { useI18n } from 'vue-i18n'
import {
  PlayCircleOutlined,
  PauseCircleOutlined,
  ReloadOutlined,
  FolderOpenOutlined,
  DeleteOutlined
} from '@ant-design/icons-vue'

defineProps({
  tasks: {
    type: Array as PropType<DownloadTask[]>,
    required: true
  }
})

const emit = defineEmits<{
  action: [payload: { action: string, taskId: string }]
}>()

const { t } = useI18n()

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    waiting: 'default',
    downloading: 'processing',
    completed: 'success',
    failed: 'error',
    paused: 'warning'
  }
  return colors[status] || 'default'
}

const getStatusText = (status: string) => {
  const texts: Record<string, string> = {
    waiting: t('home.status.waiting'),
    downloading: t('home.status.downloading'),
    completed: t('home.status.completed'),
    failed: t('home.status.failed'),
    paused: t('home.status.paused')
  }
  return texts[status] || status
}
</script>

<style scoped>
</style>
