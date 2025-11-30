<template>
  <div>
    <a-card :title="$t('settings.general.title')" :bordered="false">
      <a-form :model="formState" layout="vertical">
        <a-divider orientation="left">{{ $t('settings.general.downloadSettings') }}</a-divider>
        
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item :label="$t('settings.general.defaultSavePath')">
              <a-input v-model:value="formState.savePath" readonly>
                <template #suffix>
                  <a-button type="link" size="small">{{ $t('addTask.browse') }}</a-button>
                </template>
              </a-input>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item :label="$t('settings.general.defaultQuality')">
              <a-select v-model:value="formState.defaultQuality" size="large">
                <a-select-option value="best">{{ $t('addTask.qualities.best') }}</a-select-option>
                <a-select-option value="1080p">{{ $t('addTask.qualities.1080p') }}</a-select-option>
                <a-select-option value="720p">{{ $t('addTask.qualities.720p') }}</a-select-option>
                <a-select-option value="480p">{{ $t('addTask.qualities.480p') }}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item :label="$t('settings.general.maxConcurrent')">
              <a-input-number v-model:value="formState.maxConcurrent" :min="1" :max="10" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item :label="$t('settings.general.speedLimit')">
              <a-input-number v-model:value="formState.speedLimit" :min="0" :max="100" :placeholder="$t('settings.general.speedLimitPlaceholder')" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-form-item>
          <a-checkbox v-model:checked="formState.autoStart">{{ $t('settings.general.autoStart') }}</a-checkbox>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model:checked="formState.autoRetry">{{ $t('settings.general.autoRetry') }}</a-checkbox>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model:checked="formState.deleteAfterComplete">{{ $t('settings.general.deleteAfterComplete') }}</a-checkbox>
        </a-form-item>

        <a-divider orientation="left">{{ $t('settings.general.appSettings') }}</a-divider>

        <a-form-item :label="$t('settings.general.language')">
          <a-select v-model:value="formState.language" size="large">
            <a-select-option value="zh-CN">简体中文</a-select-option>
            <a-select-option value="zh-TW">繁体中文</a-select-option>
            <a-select-option value="en-US">English</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item :label="$t('settings.general.theme')">
          <a-radio-group v-model:value="formState.theme">
            <a-radio value="light">{{ $t('settings.general.themeLight') }}</a-radio>
            <a-radio value="dark">{{ $t('settings.general.themeDark') }}</a-radio>
            <a-radio value="auto">{{ $t('settings.general.themeAuto') }}</a-radio>
          </a-radio-group>
        </a-form-item>

        <a-form-item>
          <a-checkbox v-model:checked="formState.autoUpdate">{{ $t('settings.general.autoUpdate') }}</a-checkbox>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model:checked="formState.startOnBoot">{{ $t('settings.general.startOnBoot') }}</a-checkbox>
        </a-form-item>
        <a-form-item>
          <a-checkbox v-model:checked="formState.minimizeToTray">{{ $t('settings.general.minimizeToTray') }}</a-checkbox>
        </a-form-item>

        <a-divider />

        <a-form-item>
          <a-space>
            <a-button type="primary" @click="handleSave">
              <SaveOutlined />
              {{ $t('settings.general.saveButton') }}
            </a-button>
            <a-button @click="handleReset">
              <ReloadOutlined />
              {{ $t('settings.general.restoreDefaults') }}
            </a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { SaveOutlined, ReloadOutlined } from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'

const { t } = useI18n()

const formState = reactive({
  savePath: '/Users/Downloads',
  defaultQuality: 'best',
  maxConcurrent: 3,
  speedLimit: 0,
  autoStart: true,
  autoRetry: true,
  deleteAfterComplete: false,
  language: 'zh-CN',
  theme: 'light',
  autoUpdate: true,
  startOnBoot: false,
  minimizeToTray: true
})

const handleSave = () => {
  // 保存设置到本地存储
  localStorage.setItem('settings', JSON.stringify(formState))
  message.success(t('settings.general.saveSuccess'))
}

const handleReset = () => {
  formState.savePath = '/Users/Downloads'
  formState.defaultQuality = 'best'
  formState.maxConcurrent = 3
  formState.speedLimit = 0
  formState.autoStart = true
  formState.autoRetry = true
  formState.deleteAfterComplete = false
  formState.language = 'zh-CN'
  formState.theme = 'light'
  formState.autoUpdate = true
  formState.startOnBoot = false
  formState.minimizeToTray = true
  message.info(t('settings.general.restored'))
}
</script>

<style scoped>
</style>
