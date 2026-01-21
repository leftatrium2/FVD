<template>
  <div class="home-container">
    <h1>{{ $t('home.welcome') }}</h1>
    <el-card>
      <template #header>
        <div class="card-header">
          <span>{{ $t('home.title') }}</span>
        </div>
      </template>
      <p>This is the home page of Full Video Downloader.</p>
    </el-card>
  </div>
</template>

<style scoped>
.home-container {
  padding: 20px;
}
</style>
