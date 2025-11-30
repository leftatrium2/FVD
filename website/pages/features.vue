<template>
  <div class="page features-page">
    <h1>{{ $t('features.title') }}</h1>
  </div>
</template>

<script setup>
const { t } = useI18n()

useSeoMeta({
  title: () => `${t('features.title')} - iVD`,
  description: 'iVD视频下载工具的强大特性'
})
</script>
