<template>
  <div class="page download-page">
    <h1>{{ $t('download.title') }}</h1>
  </div>
</template>

<script setup>
const { t } = useI18n()

useSeoMeta({
  title: () => `${t('download.title')} - iVD`,
  description: '下载iVD视频下载工具'
})
</script>
