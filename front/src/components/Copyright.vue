<template>
  <div class="copyright-container">
    <p class="copyright-text">
      {{ $t('common.copyright') }}
    </p>
  </div>
</template>

<script setup lang="ts">
// Copyright component
</script>

<style scoped>
.copyright-container {
  text-align: center;
  padding: 16px 0;
  margin-top: 24px;
  border-top: 1px solid #f0f0f0;
}

.copyright-text {
  color: #999;
  font-size: 12px;
  margin: 0;
}
</style>
