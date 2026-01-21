<template>
  <el-container class="layout-container">
    <el-aside width="200px">
      <el-menu
        :default-active="activePath"
        class="el-menu-vertical"
        router
      >
        <el-menu-item index="/home">
          <el-icon><VideoCamera /></el-icon>
          <span>{{ $t('menu.home') }}</span>
        </el-menu-item>
        <el-menu-item index="/download">
          <el-icon><Download /></el-icon>
          <span>{{ $t('menu.download') }}</span>
        </el-menu-item>
        <el-menu-item index="/add-single-task">
          <el-icon><Plus /></el-icon>
          <span>{{ $t('menu.addSingleTask') }}</span>
        </el-menu-item>
        <el-menu-item index="/add-scheduled-task">
          <el-icon><Calendar /></el-icon>
          <span>{{ $t('menu.addScheduledTask') }}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="header">
        <div class="header-left">
          <h2>{{ $t('home.title') }}</h2>
        </div>
        <div class="header-right">
          <el-dropdown @command="handleLanguageChange">
            <span class="el-dropdown-link">
              {{ $t('common.language') }}: {{ currentLocaleName }}
              <el-icon class="el-icon--right"><arrow-down /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="zh">{{ $t('common.chinese') }}</el-dropdown-item>
                <el-dropdown-item command="en">{{ $t('common.english') }}</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

const route = useRoute()
const { locale, t } = useI18n()

const activePath = computed(() => route.path)

const currentLocaleName = computed(() => {
  return locale.value === 'zh' ? t('common.chinese') : t('common.english')
})

const handleLanguageChange = (lang: string) => {
  locale.value = lang
}
</script>

<style scoped>
.layout-container {
  height: 100vh;
}
.el-menu-vertical {
  height: 100%;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  background-color: #fff;
}
.header-right {
  display: flex;
  align-items: center;
}
.el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
</style>
