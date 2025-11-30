<template>
  <div>
    <a-card :bordered="false">
      <div class="text-center py-12">
        <div class="mb-8">
          <h1 class="text-5xl font-bold text-blue-600 mt-4">FVD</h1>
          <p class="text-xl text-gray-500 mt-2">{{ $t('settings.about.subtitle') }}</p>
        </div>

        <a-descriptions bordered :column="1" class="max-w-2xl mx-auto mb-8">
          <a-descriptions-item :label="$t('settings.about.versionLabel')">
            v1.0.0
          </a-descriptions-item>
          <a-descriptions-item :label="$t('settings.about.releaseDateLabel')">
            2025-11-22
          </a-descriptions-item>
          <a-descriptions-item :label="$t('settings.about.developerLabel')">
            FVD Team
          </a-descriptions-item>
          <a-descriptions-item :label="$t('settings.about.websiteLabel')">
            <a href="https://fullvideodown.com" target="_blank" class="text-blue-600">
              https://fullvideodown.com
            </a>
          </a-descriptions-item>
          <a-descriptions-item :label="$t('settings.about.supportLabel')">
            support@fullvideodown.com
          </a-descriptions-item>
        </a-descriptions>

        <a-divider />

        <div class="max-w-2xl mx-auto text-left mb-8">
          <h3 class="text-xl font-bold mb-4">{{ $t('settings.about.productIntro') }}</h3>
          <p class="text-gray-600 leading-relaxed mb-4">
            {{ $t('settings.about.intro1') }}
          </p>
          <p class="text-gray-600 leading-relaxed mb-4">
            {{ $t('settings.about.intro2') }}
          </p>

          <h3 class="text-xl font-bold mb-4 mt-6">{{ $t('settings.about.keyFeatures') }}</h3>
          <ul class="text-gray-600 space-y-2">
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature1') }}
            </li>
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature2') }}
            </li>
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature3') }}
            </li>
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature4') }}
            </li>
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature5') }}
            </li>
            <li class="flex items-center">
              <CheckCircleOutlined class="text-green-500 mr-2" />
              {{ $t('settings.about.features.feature6') }}
            </li>
          </ul>
        </div>

        <a-divider />

        <div class="mb-6">
          <a-space size="large">
            <a-button type="primary" size="large" @click="checkUpdate">
              <SyncOutlined />
              {{ $t('settings.about.checkUpdate') }}
            </a-button>
            <a-button size="large">
              <GithubOutlined />
              {{ $t('settings.about.visitGithub') }}
            </a-button>
            <a-button size="large">
              <FileTextOutlined />
              {{ $t('settings.about.viewDocs') }}
            </a-button>
          </a-space>
        </div>
      </div>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import {
  CheckCircleOutlined,
  SyncOutlined,
  GithubOutlined,
  FileTextOutlined
} from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'

const { t } = useI18n()

const checkUpdate = () => {
  message.loading(t('settings.about.checkingUpdate'), 2).then(() => {
    message.success(t('settings.about.alreadyLatest'))
  })
}
</script>

<style scoped>
</style>
