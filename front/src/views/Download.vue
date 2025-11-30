<template>
  <div>
    <div class="mb-6 flex items-center justify-between">
      <h2 class="text-2xl font-bold">{{ $t('download.title') }}</h2>
      <a-space>
        <a-button type="primary" @click="goToAddTask">
          <PlusOutlined />
          {{ $t('download.newTask') }}
        </a-button>
        <a-button @click="startAll">
          <PlayCircleOutlined />
          {{ $t('download.startAll') }}
        </a-button>
        <a-button @click="pauseAll">
          <PauseCircleOutlined />
          {{ $t('download.pauseAll') }}
        </a-button>
        <a-button danger @click="clearCompleted">
          <DeleteOutlined />
          {{ $t('download.clearCompleted') }}
        </a-button>
      </a-space>
    </div>

    <a-card :bordered="false">
      <a-tabs v-model:activeKey="activeTab">
        <a-tab-pane key="all" :tab="$t('download.tabs.all')">
          <TaskList :tasks="allTasks" @action="handleAction" />
        </a-tab-pane>
        <a-tab-pane key="downloading" :tab="$t('download.tabs.downloading')">
          <TaskList :tasks="downloadingTasks" @action="handleAction" />
        </a-tab-pane>
        <a-tab-pane key="completed" :tab="$t('download.tabs.completed')">
          <TaskList :tasks="completedTasks" @action="handleAction" />
        </a-tab-pane>
        <a-tab-pane key="failed" :tab="$t('download.tabs.failed')">
          <TaskList :tasks="failedTasks" @action="handleAction" />
        </a-tab-pane>
      </a-tabs>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useDownloadStore } from '@/store/download'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'
import {
  PlusOutlined,
  PlayCircleOutlined,
  PauseCircleOutlined,
  DeleteOutlined
} from '@ant-design/icons-vue'
import { message, Modal } from 'ant-design-vue'
import TaskList from '@/components/TaskList.vue'

const router = useRouter()
const downloadStore = useDownloadStore()
const { t } = useI18n()

const activeTab = ref('all')

const allTasks = computed(() => downloadStore.tasks)
const downloadingTasks = computed(() => 
  downloadStore.tasks.filter(t => t.status === 'downloading' || t.status === 'waiting')
)
const completedTasks = computed(() => 
  downloadStore.tasks.filter(t => t.status === 'completed')
)
const failedTasks = computed(() => 
  downloadStore.tasks.filter(t => t.status === 'failed')
)

const goToAddTask = () => {
  router.push('/add-single-task')
}

const startAll = () => {
  downloadStore.tasks.forEach(task => {
    if (task.status === 'paused' || task.status === 'waiting') {
      downloadStore.updateTask(task.id, { status: 'downloading' })
    }
  })
  message.success(t('download.allStarted'))
}

const pauseAll = () => {
  downloadStore.tasks.forEach(task => {
    if (task.status === 'downloading') {
      downloadStore.updateTask(task.id, { status: 'paused' })
    }
  })
  message.success(t('download.allPaused'))
}

const clearCompleted = () => {
  Modal.confirm({
    title: t('download.confirmClear'),
    content: t('download.confirmClearContent'),
    okText: t('common.confirm'),
    cancelText: t('common.cancel'),
    onOk: () => {
      const completedIds = downloadStore.tasks
        .filter(t => t.status === 'completed')
        .map(t => t.id)
      completedIds.forEach(id => downloadStore.removeTask(id))
      message.success(t('download.cleared'))
    }
  })
}

const handleAction = ({ action, taskId }: { action: string, taskId: string }) => {
  const task = downloadStore.tasks.find(t => t.id === taskId)
  if (!task) return

  switch (action) {
    case 'start':
      downloadStore.updateTask(taskId, { status: 'downloading' })
      message.success(t('download.taskStarted'))
      break
    case 'pause':
      downloadStore.updateTask(taskId, { status: 'paused' })
      message.success(t('download.taskPaused'))
      break
    case 'retry':
      downloadStore.updateTask(taskId, { status: 'downloading', progress: 0 })
      message.success(t('download.taskRetried'))
      break
    case 'delete':
      Modal.confirm({
        title: t('download.confirmDelete'),
        content: t('download.confirmDeleteContent', { title: task.title }),
        okText: t('common.confirm'),
        cancelText: t('common.cancel'),
        onOk: () => {
          downloadStore.removeTask(taskId)
          message.success(t('download.taskDeleted'))
        }
      })
      break
  }
}
</script>

<style scoped>
</style>
