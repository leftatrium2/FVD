import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    tasks: [],
    settings: {
      downloadPath: '',
    },
  }),
  actions: {
    addTask(task: any) {
      this.tasks.push(task as never)
    },
  },
})
