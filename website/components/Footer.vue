<template>
  <footer class="footer">
    <div class="footer-container">
      <p>{{ $t('footer.copyright') }}</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #333;
  color: #fff;
  padding: 2rem 1rem;
  margin-top: auto;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.footer-container p {
  margin: 0;
  font-size: 0.9rem;
  opacity: 0.9;
}
</style>
