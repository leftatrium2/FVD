<template>
  <div>
    <a-card :bordered="false">
      <div class="text-center py-12">
        <div class="mb-8">
          <CrownOutlined class="text-yellow-500" style="font-size: 80px;" />
        </div>
        
        <h2 class="text-3xl font-bold mb-4">{{ $t('settings.upgrade.title') }}</h2>
        <p class="text-gray-500 mb-8 text-lg">{{ $t('settings.upgrade.subtitle') }}</p>

        <a-row :gutter="24" class="mb-12">
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <ThunderboltOutlined class="feature-icon text-blue-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.highSpeed') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.highSpeedDesc') }}</p>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <CloudServerOutlined class="feature-icon text-green-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.cloudStorage') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.cloudStorageDesc') }}</p>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <SafetyOutlined class="feature-icon text-purple-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.adFree') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.adFreeDesc') }}</p>
            </a-card>
          </a-col>
        </a-row>

        <a-row :gutter="24" class="mb-12">
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <TeamOutlined class="feature-icon text-red-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.batchDownload') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.batchDownloadDesc') }}</p>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <ScheduleOutlined class="feature-icon text-orange-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.scheduledDownload') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.scheduledDownloadDesc') }}</p>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card hoverable class="feature-card">
              <CustomerServiceOutlined class="feature-icon text-indigo-500" />
              <h3 class="mt-4 mb-2 font-bold">{{ $t('settings.upgrade.features.prioritySupport') }}</h3>
              <p class="text-gray-500">{{ $t('settings.upgrade.features.prioritySupportDesc') }}</p>
            </a-card>
          </a-col>
        </a-row>

        <a-divider />

        <h3 class="text-2xl font-bold mb-6">{{ $t('settings.upgrade.choosePlan') }}</h3>
        
        <a-row :gutter="24" justify="center">
          <a-col :span="6">
            <a-card hoverable class="price-card">
              <h4 class="text-xl font-bold mb-2">{{ $t('settings.upgrade.plans.monthly') }}</h4>
              <div class="price mb-4">
                <span class="text-4xl font-bold">{{ $t('settings.upgrade.plans.monthlyPrice') }}</span>
                <span class="text-gray-500">{{ $t('settings.upgrade.plans.perMonth') }}</span>
              </div>
              <a-button type="default" size="large" block>
                {{ $t('settings.upgrade.subscribe') }}
              </a-button>
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card hoverable class="price-card border-2 border-blue-500">
              <a-badge-ribbon :text="$t('settings.upgrade.recommended')" color="blue">
                <h4 class="text-xl font-bold mb-2">{{ $t('settings.upgrade.plans.yearly') }}</h4>
                <div class="price mb-4">
                  <span class="text-4xl font-bold text-blue-600">{{ $t('settings.upgrade.plans.yearlyPrice') }}</span>
                  <span class="text-gray-500">{{ $t('settings.upgrade.plans.perYear') }}</span>
                  <div class="text-sm text-green-600 mt-1">{{ $t('settings.upgrade.plans.yearlySave') }}</div>
                </div>
                <a-button type="primary" size="large" block>
                  {{ $t('settings.upgrade.subscribe') }}
                </a-button>
              </a-badge-ribbon>
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card hoverable class="price-card">
              <h4 class="text-xl font-bold mb-2">{{ $t('settings.upgrade.plans.lifetime') }}</h4>
              <div class="price mb-4">
                <span class="text-4xl font-bold">{{ $t('settings.upgrade.plans.lifetimePrice') }}</span>
                <span class="text-gray-500"></span>
              </div>
              <a-button type="default" size="large" block>
                {{ $t('settings.upgrade.buyNow') }}
              </a-button>
            </a-card>
          </a-col>
        </a-row>

        <div class="mt-8 text-gray-500 text-sm">
          <p>{{ $t('settings.upgrade.refundPolicy') }}</p>
          <p>{{ $t('settings.upgrade.paymentMethods') }}</p>
        </div>
      </div>
    </a-card>
    
    <Copyright />
  </div>
</template>

<script setup lang="ts">
import {
  CrownOutlined,
  ThunderboltOutlined,
  CloudServerOutlined,
  SafetyOutlined,
  TeamOutlined,
  ScheduleOutlined,
  CustomerServiceOutlined
} from '@ant-design/icons-vue'
import Copyright from '@/components/Copyright.vue'
</script>

<style scoped>
.feature-icon {
  font-size: 48px;
}

.feature-card {
  text-align: center;
  transition: all 0.3s;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.price-card {
  text-align: center;
  padding: 20px 0;
}
</style>
