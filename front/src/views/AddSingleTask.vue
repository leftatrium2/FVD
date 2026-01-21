<template>
  <div>
    <a-card :bordered="false" class="max-w-6xl mx-auto">
      <div class="mb-6">
        <div class="mb-2">
          <span class="text-base whitespace-nowrap">{{ $t('addSingleTask.linkLabel') }}</span>
          <a-tooltip placement="top">
            <template #title>
              <div>{{ $t('addSingleTask.linkTip') }}</div>
            </template>
            <QuestionCircleOutlined class="ml-2 text-gray-400 cursor-pointer hover:text-blue-500" />
          </a-tooltip>
        </div>
        
        <div class="flex gap-4 mb-6">
          <a-textarea
            v-model:value="url"
            size="large"
            :placeholder="$t('addSingleTask.urlPlaceholder')"
            :auto-size="{ minRows: 4, maxRows: 8 }"
            style="flex: 1"
          />
          <div class="flex items-start">
            <a-button type="primary" size="large" @click="handleDetect" :loading="detecting" class="px-8">
              {{ $t('addSingleTask.detectButton') }}
            </a-button>
          </div>
        </div>

        <div class="flex items-center gap-4">
          <span class="text-base whitespace-nowrap">{{ $t('addSingleTask.videoQuality') }}</span>
          <a-select v-model:value="quality" size="large" style="width: 200px">
            <a-select-option :value="0">{{ $t('addSingleTask.qualityOptions.default') }}</a-select-option>
            <a-select-option :value="1">{{ $t('addSingleTask.qualityOptions.best') }}</a-select-option>
            <a-select-option :value="2">{{ $t('addSingleTask.qualityOptions.fast') }}</a-select-option>
          </a-select>
        </div>
      </div>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { QuestionCircleOutlined } from '@ant-design/icons-vue'
import Copyright from '@/components/Copyright.vue'
import { message } from 'ant-design-vue'
import request from '@/utils/request'

const { t } = useI18n()

const url = ref('')
const quality = ref(0)
const detecting = ref(false)

const handleDetect = async () => {
  if (!url.value.trim()) {
    message.warning(t('addSingleTask.urlRequired'))
    return
  }
  
  // 按换行符分割链接，过滤掉空行
  const urls = url.value
    .split('\n')
    .map((line: string) => line.trim())
    .filter((line: string) => line.length > 0)
  
  if (urls.length === 0) {
    message.warning(t('addSingleTask.urlRequired'))
    return
  }
  
  detecting.value = true
  
  try {
    const payload = {
      quality: quality.value,
      url: urls
    }
    const response = await request.post('/task/simple', payload)
    
    if (response.code === 0) {
      message.success(t('addSingleTask.detectSuccess'))
      // 下载成功后清空输入框
      url.value = ''
    } else {
      message.error(response.msg || t('addSingleTask.detectFailed'))
    }
  } catch (error) {
    console.error('下载失败:', error)
    message.error(t('addSingleTask.detectFailed'))
  } finally {
    detecting.value = false
  }
}
</script>

<style scoped>
</style>
