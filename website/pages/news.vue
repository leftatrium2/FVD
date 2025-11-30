<template>
  <div class="page news-page">
    <h1>{{ $t('news.title') }}</h1>
  </div>
</template>

<script setup>
const { t } = useI18n()

useSeoMeta({
  title: () => `${t('news.title')} - iVD`,
  description: 'iVD最新新闻和更新'
})
</script>
