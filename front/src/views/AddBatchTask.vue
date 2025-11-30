<template>
  <div>
    <a-card :title="$t('addBatchTask.title')" class="max-w-4xl mx-auto">
      <a-form
        :model="formState"
        name="add-batch-task"
        layout="vertical"
        @finish="onFinish"
      >
        <a-form-item
          :label="$t('addBatchTask.urls')"
          name="urls"
          :rules="[{ required: true, message: $t('addBatchTask.urlsRequired') }]"
        >
          <a-textarea
            v-model:value="formState.urls"
            :rows="8"
            :placeholder="$t('addBatchTask.urlsPlaceholder')"
          />
        </a-form-item>

        <a-row :gutter="16">
          <a-col :span="8">
            <a-form-item :label="$t('addSingleTask.quality')" name="quality">
              <a-select v-model:value="formState.quality" size="large">
                <a-select-option value="best">{{ $t('addSingleTask.qualities.best') }}</a-select-option>
                <a-select-option value="1080p">{{ $t('addSingleTask.qualities.1080p') }}</a-select-option>
                <a-select-option value="720p">{{ $t('addSingleTask.qualities.720p') }}</a-select-option>
                <a-select-option value="480p">{{ $t('addSingleTask.qualities.480p') }}</a-select-option>
                <a-select-option value="360p">{{ $t('addSingleTask.qualities.360p') }}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-form-item :label="$t('addSingleTask.savePath')" name="savePath">
              <a-input
                v-model:value="formState.savePath"
                size="large"
                :placeholder="$t('addSingleTask.savePathPlaceholder')"
                readonly
              >
                <template #suffix>
                  <a-button type="link" size="small" @click="selectFolder">
                    {{ $t('addSingleTask.browse') }}
                  </a-button>
                </template>
              </a-input>
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-form-item :label="$t('addBatchTask.concurrent')" name="concurrent">
              <a-input-number
                v-model:value="formState.concurrent"
                :min="1"
                :max="10"
                size="large"
                style="width: 100%"
              />
            </a-form-item>
          </a-col>
        </a-row>

        <a-form-item>
          <a-space>
            <a-checkbox v-model:checked="formState.autoStart">
              {{ $t('addSingleTask.autoStart') }}
            </a-checkbox>
            <a-checkbox v-model:checked="formState.parsePlaylist">
              {{ $t('addSingleTask.parsePlaylist') }}
            </a-checkbox>
            <a-checkbox v-model:checked="formState.autoRename">
              {{ $t('addBatchTask.autoRename') }}
            </a-checkbox>
          </a-space>
        </a-form-item>

        <a-divider />

        <a-alert
          v-if="urlCount > 0"
          :message="$t('addBatchTask.detectedLinks', { count: urlCount })"
          type="info"
          show-icon
          class="mb-4"
        />

        <a-form-item>
          <a-space>
            <a-button type="primary" html-type="submit" size="large" :loading="loading">
              <PlusCircleOutlined />
              {{ $t('addBatchTask.batchAdd', { count: urlCount }) }}
            </a-button>
            <a-button size="large" @click="reset">
              <ReloadOutlined />
              {{ $t('common.reset') }}
            </a-button>
            <a-button size="large" @click="goBack">
              {{ $t('common.cancel') }}
            </a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useDownloadStore } from '@/store/download'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'
import {
  PlusCircleOutlined,
  ReloadOutlined
} from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'

const router = useRouter()
const downloadStore = useDownloadStore()
const { t } = useI18n()

const formState = reactive({
  urls: '',
  quality: 'best',
  savePath: '/Users/Downloads',
  concurrent: 3,
  autoStart: true,
  parsePlaylist: false,
  autoRename: true
})

const loading = ref(false)

const urlCount = computed(() => {
  const urls = formState.urls.split('\n').filter(url => url.trim())
  return urls.length
})

const selectFolder = () => {
  message.info(t('addBatchTask.selectFolder'))
}

const onFinish = async (values: any) => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 500))
    
    const urls = values.urls.split('\n').filter((url: string) => url.trim())
    
    urls.forEach((url: string, index: number) => {
      downloadStore.addTask({
        url: url.trim(),
        title: `${t('addBatchTask.title')} ${index + 1}`,
        status: values.autoStart ? 'waiting' : 'waiting',
        progress: 0
      })
    })
    
    message.success(t('addBatchTask.addSuccess', { count: urls.length }))
    router.push('/download')
  } catch (error) {
    message.error(t('addSingleTask.addFailed'))
  } finally {
    loading.value = false
  }
}

const reset = () => {
  formState.urls = ''
  formState.quality = 'best'
  formState.savePath = '/Users/Downloads'
  formState.concurrent = 3
  formState.autoStart = true
  formState.parsePlaylist = false
  formState.autoRename = true
}

const goBack = () => {
  router.back()
}
</script>

<style scoped>
</style>
