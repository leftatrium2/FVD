<template>
  <header class="header">
    <div class="header-container">
      <div class="logo">
        <NuxtLink to="/">
          <span class="brand-short">{{ $t('brand.short') }}</span>
          <span class="brand-name">{{ $t('brand.name') }}</span>
        </NuxtLink>
      </div>
      
      <nav class="nav">
        <NuxtLink to="/" class="nav-link">{{ $t('nav.home') }}</NuxtLink>
        <NuxtLink to="/news" class="nav-link">{{ $t('nav.news') }}</NuxtLink>
        <NuxtLink to="/features" class="nav-link">{{ $t('nav.features') }}</NuxtLink>
        <NuxtLink to="/download" class="nav-link">{{ $t('nav.download') }}</NuxtLink>
        <NuxtLink to="/support" class="nav-link">{{ $t('nav.support') }}</NuxtLink>
        
        <div class="language-selector">
          <select v-model="currentLocale" @change="changeLanguage" class="language-dropdown">
            <option value="zh">{{ $t('language.chinese') }}</option>
            <option value="en">{{ $t('language.english') }}</option>
          </select>
        </div>
      </nav>
    </div>
  </header>
</template>

<script setup>
const { locale, setLocale } = useI18n()
const currentLocale = ref(locale.value)

const changeLanguage = () => {
  setLocale(currentLocale.value)
}

// 监听locale变化，同步到currentLocale
watch(locale, (newLocale) => {
  currentLocale.value = newLocale
})
</script>

<style scoped>
.header {
  background-color: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
}

.logo a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: bold;
}

.brand-short {
  font-size: 1.8rem;
  color: #4CAF50;
}

.brand-name {
  font-size: 1rem;
  color: #333;
}

.nav {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  color: #333;
  font-weight: 500;
  transition: color 0.3s;
  position: relative;
}

.nav-link:hover {
  color: #4CAF50;
}

.nav-link.router-link-active,
.nav-link.router-link-exact-active {
  color: #4CAF50;
}

.nav-link.router-link-active::after,
.nav-link.router-link-exact-active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #4CAF50;
}

.language-selector {
  margin-left: 1rem;
}

.language-dropdown {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #fff;
  color: #333;
  font-size: 0.9rem;
  cursor: pointer;
  transition: border-color 0.3s;
}

.language-dropdown:hover {
  border-color: #4CAF50;
}

.language-dropdown:focus {
  outline: none;
  border-color: #4CAF50;
}

@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    height: auto;
    padding: 1rem;
  }
  
  .nav {
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1rem;
    justify-content: center;
  }
  
  .brand-name {
    display: none;
  }
}
</style>
