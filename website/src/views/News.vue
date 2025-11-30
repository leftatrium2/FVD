<template>
  <div class="page news-page">
    <h1>{{ $t('news.title') }}</h1>
    <p class="description">{{ $t('news.description') }}</p>
  </div>
</template>

<style scoped>
.page {
  min-height: 400px;
}

h1 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 2.5rem;
}

.description {
  font-size: 1.2rem;
  color: #666;
}
</style>
