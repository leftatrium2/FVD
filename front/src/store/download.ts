import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface DownloadTask {
  id: string
  url: string
  title: string
  status: 'waiting' | 'downloading' | 'completed' | 'failed' | 'paused'
  progress: number
  speed?: string
  size?: string
  createdAt: Date
}

export const useDownloadStore = defineStore('download', () => {
  const tasks = ref<DownloadTask[]>([])

  const addTask = (task: Omit<DownloadTask, 'id' | 'createdAt'>) => {
    const newTask: DownloadTask = {
      ...task,
      id: Date.now().toString(),
      createdAt: new Date()
    }
    tasks.value.unshift(newTask)
    return newTask
  }

  const removeTask = (id: string) => {
    const index = tasks.value.findIndex(t => t.id === id)
    if (index > -1) {
      tasks.value.splice(index, 1)
    }
  }

  const updateTask = (id: string, updates: Partial<DownloadTask>) => {
    const task = tasks.value.find(t => t.id === id)
    if (task) {
      Object.assign(task, updates)
    }
  }

  return {
    tasks,
    addTask,
    removeTask,
    updateTask
  }
})
