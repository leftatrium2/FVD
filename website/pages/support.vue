<template>
  <div class="page support-page">
    <h1>{{ $t('support.title') }}</h1>
  </div>
</template>

<script setup>
const { t } = useI18n()

useSeoMeta({
  title: () => `${t('support.title')} - iVD`,
  description: 'iVD技术支持和帮助中心'
})
</script>
