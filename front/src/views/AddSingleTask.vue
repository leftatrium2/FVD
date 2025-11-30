<template>
  <div>
    <a-card :bordered="false" class="max-w-6xl mx-auto">
      <div class="flex items-center gap-4 mb-6">
        <span class="text-base whitespace-nowrap">{{ $t('addSingleTask.linkLabel') }}</span>
        <a-input
          v-model:value="url"
          size="large"
          :placeholder="$t('addSingleTask.urlPlaceholder')"
          style="flex: 1"
        />
        <a-button type="primary" size="large" @click="handleDetect" :loading="detecting">
          {{ $t('addSingleTask.detectButton') }}
        </a-button>
      </div>

      <!-- 检测结果显示区域 -->
      <div v-if="videoInfo" class="mt-6">
        <div class="flex gap-6">
          <!-- 缩略图 -->
          <div class="flex-shrink-0">
            <img 
              :src="videoInfo.thumbnails" 
              :alt="videoInfo.title"
              class="w-96 h-auto rounded-lg object-cover border-2 border-blue-500"
            />
          </div>
          <!-- 视频信息 -->
          <div class="flex-1">
            <h3 class="text-xl font-semibold mb-4">{{ videoInfo.title }}</h3>
            <div class="space-y-2 text-base">
              <div>{{ videoInfo.channel }}  {{ formatDate(videoInfo.upload_date) }}</div>
            </div>
          </div>
        </div>
        
        <!-- 操作按钮 -->
        <div class="flex gap-4 mt-6 justify-center">
          <a-button size="large" style="width: 120px" @click="handleDownload">
            {{ $t('addSingleTask.downloadButton') }}
          </a-button>
          <a-button size="large" style="width: 120px" @click="handleCancel">
            {{ $t('common.cancel') }}
          </a-button>
        </div>
      </div>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'
import { message } from 'ant-design-vue'
import request from '@/utils/request'

const { t } = useI18n()

interface VideoInfo {
  channel: string
  thumbnails: string
  title: string
  upload_date: string
}

const url = ref('')
const detecting = ref(false)
const videoInfo = ref<VideoInfo | null>(null)

const handleDetect = async () => {
  if (!url.value.trim()) {
    message.warning(t('addSingleTask.urlRequired'))
    return
  }
  
  detecting.value = true
  videoInfo.value = null
  
  try {
    const response = await request.post('/task/simple/first', {
      url: url.value
    })
    
    if (response.code === 0) {
      videoInfo.value = response.data
      message.success(t('addSingleTask.detectSuccess'))
    } else {
      message.error(response.msg || t('addSingleTask.detectFailed'))
    }
  } catch (error) {
    console.error('棄测失败:', error)
    message.error(t('addSingleTask.detectFailed'))
  } finally {
    detecting.value = false
  }
}

// 格式化上传日期
const formatDate = (dateStr: string) => {
  if (!dateStr || dateStr.length !== 8) return dateStr
  // 将 20250926 转换为 2025-09-26
  const year = dateStr.substring(0, 4)
  const month = dateStr.substring(4, 6)
  const day = dateStr.substring(6, 8)
  return `${year}-${month}-${day}`
}

// 处理下载按钮
const handleDownload = () => {
  if (videoInfo.value) {
    message.success(t('addSingleTask.downloadStarted'))
    // 这里添加下载逻辑
  }
}

// 处理取消按钮
const handleCancel = () => {
  videoInfo.value = null
  url.value = ''
}
</script>

<style scoped>
</style>
