<template>
  <div class="page support-page">
    <h1>{{ $t('support.title') }}</h1>
    <p class="description">{{ $t('support.description') }}</p>
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
