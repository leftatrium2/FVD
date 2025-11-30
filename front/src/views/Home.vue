<template>
  <div>
    <!-- 顶部搜索栏 -->
    <div class="mb-6">
      <a-card :bordered="false">
        <div class="flex items-center gap-4">
          <a-select
            v-model:value="libraryType"
            style="width: 200px"
            :loading="libraryLoading"
          >
            <!-- 当有素材库数据时，展示接口返回的数据 -->
            <template v-if="libraryList.length > 0">
              <a-select-option v-for="library in libraryList" :key="library.name" :value="library.name">
                {{ library.description }}
              </a-select-option>
            </template>
            <!-- 当没有数据时，展示“全部素材库” -->
            <a-select-option v-else value="all">{{ $t('home.libraryType') }}</a-select-option>
          </a-select>
          <a-input
            v-model:value="keyword"
            :placeholder="$t('home.searchPlaceholder')"
            style="flex: 1"
          />
          <a-button type="primary" @click="handleSearch">
            {{ $t('home.confirm') }}
          </a-button>
          <a-select
            v-model:value="viewMode"
            style="width: 150px"
            @change="handleViewModeChange"
          >
            <a-select-option value="simple">{{ $t('home.simpleView') }}</a-select-option>
            <a-select-option value="complex">{{ $t('home.complexView') }}</a-select-option>
          </a-select>
        </div>
      </a-card>
    </div>

    <!-- 复杂界面 -->
    <div v-if="viewMode === 'complex'">
      <a-card :title="$t('home.complexList')" :bordered="false">
        <a-table
          :columns="complexColumns"
          :data-source="dataSource"
          :pagination="pagination"
          :loading="loading"
          @change="handleTableChange"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'video'">
              <div class="flex items-center justify-center">
                <div class="w-24 h-16 bg-gray-200 rounded flex items-center justify-center">
                  <PlayCircleOutlined class="text-3xl text-white" />
                </div>
              </div>
            </template>
            <template v-else-if="column.key === 'audio'">
              <div class="flex items-center justify-center">
                <a-button size="small" type="text">
                  >
                </a-button>
              </div>
            </template>
            <template v-else-if="column.key === 'subtitle'">
              <a-button type="link" size="small">{{ $t('home.table.watchContinue') }}</a-button>
            </template>
            <template v-else-if="column.key === 'library'">
              {{ $t('home.table.platform') }}
            </template>
            <template v-else-if="column.key === 'operation'">
              <a-button type="link" danger size="small" @click="handleDelete(record)">
                {{ $t('home.table.delete') }}
              </a-button>
            </template>
          </template>
        </a-table>
      </a-card>
    </div>

    <!-- 简单界面 -->
    <div v-else>
      <a-card :title="$t('home.simpleList')" :bordered="false">
        <a-table
          :columns="simpleColumns"
          :data-source="dataSource"
          :pagination="pagination"
          :loading="loading"
          @change="handleTableChange"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'video'">
              <div class="flex items-center justify-center">
                <div class="w-24 h-16 bg-gray-200 rounded flex items-center justify-center">
                  <PlayCircleOutlined class="text-3xl text-white" />
                </div>
              </div>
            </template>
            <template v-else-if="column.key === 'operation'">
              <a-button type="link" danger size="small" @click="handleDelete(record)">
                {{ $t('home.table.delete') }}
              </a-button>
            </template>
          </template>
        </a-table>
      </a-card>
    </div>

    <Copyright />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import Copyright from '@/components/Copyright.vue'
import { PlayCircleOutlined } from '@ant-design/icons-vue'
import { message, Modal } from 'ant-design-vue'
import axios from 'axios'

const { t } = useI18n()

interface Library {
  name: string
  description: string
}

const libraryType = ref('')
const keyword = ref('')
const viewMode = ref('simple')
const loading = ref(false)
const libraryList = ref<Library[]>([])
const libraryLoading = ref(true) // 素材库加载状态

const pagination = ref({
  current: 1,
  pageSize: 10,
  total: 50
})

// 复杂界面的列配置
const complexColumns = computed(() => [
  {
    title: t('home.table.materialId'),
    dataIndex: 'materialId',
    key: 'materialId',
    width: 150
  },
  {
    title: t('home.table.title'),
    dataIndex: 'title',
    key: 'title',
    width: 200
  },
  {
    title: t('home.table.description'),
    dataIndex: 'description',
    key: 'description',
    width: 300
  },
  {
    title: t('home.table.author'),
    dataIndex: 'author',
    key: 'author',
    width: 150
  },
  {
    title: t('home.table.video'),
    key: 'video',
    width: 150,
    align: 'center'
  },
  {
    title: t('home.table.audio'),
    key: 'audio',
    width: 100,
    align: 'center'
  },
  {
    title: t('home.table.subtitle'),
    key: 'subtitle',
    width: 120,
    align: 'center'
  },
  {
    title: t('home.table.library'),
    key: 'library',
    width: 150
  },
  {
    title: t('home.table.operation'),
    key: 'operation',
    width: 100,
    fixed: 'right'
  }
])

// 简单界面的列配置
const simpleColumns = computed(() => [
  {
    title: t('home.table.materialId'),
    dataIndex: 'materialId',
    key: 'materialId',
    width: 150
  },
  {
    title: t('home.table.title'),
    dataIndex: 'title',
    key: 'title',
    width: 200
  },
  {
    title: t('home.table.description'),
    dataIndex: 'description',
    key: 'description',
    width: 400
  },
  {
    title: t('home.table.author'),
    dataIndex: 'author',
    key: 'author',
    width: 150
  },
  {
    title: t('home.table.video'),
    key: 'video',
    width: 150,
    align: 'center'
  },
  {
    title: t('home.table.operation'),
    key: 'operation',
    width: 100,
    fixed: 'right'
  }
])

// 示例数据
const dataSource = ref([
  {
    key: '1',
    materialId: 'xJ4K0UGFS6w',
    title: '印度博主第一次来中国 竟然说出 印度很烂 我以为中国会像印度',
    description: '新闻可能只解放它想让别人知道的 大家一起来看看真正的世界 人类里的中国',
    author: 'life philosophy'
  }
])

const handleSearch = () => {
  console.log('Searching:', keyword.value, libraryType.value)
  message.info(t('home.confirm'))
}

const handleViewModeChange = (value: string) => {
  localStorage.setItem('homeViewMode', value)
  console.log('View mode changed:', value)
}

const handleTableChange = (pag: any) => {
  pagination.value = pag
}

const handleDelete = (record: any) => {
  Modal.confirm({
    title: t('download.confirmDelete'),
    content: t('download.confirmDeleteContent', { title: record.title }),
    onOk() {
      message.success(t('download.taskDeleted'))
      // 这里添加删除逻辑
    }
  })
}

// 请求素材库列表
const fetchLibraries = async () => {
  libraryLoading.value = true
  try {
    const response = await axios.get('http://localhost:9002/library')
    if (response.data.code === 0) {
      libraryList.value = response.data.data || []
      // 如果有数据，设置默认选中第一个素材库
      if (libraryList.value.length > 0) {
        libraryType.value = libraryList.value[0].name
      } else {
        libraryType.value = 'all'
      }
    } else {
      console.error('获取素材库列表失败:', response.data.msg)
      libraryList.value = []
      libraryType.value = 'all'
    }
  } catch (error) {
    console.error('请求素材库列表失败:', error)
    libraryList.value = []
    libraryType.value = 'all'
  } finally {
    libraryLoading.value = false
  }
}

onMounted(() => {
  // 从 localStorage 恢复界面模式
  const savedViewMode = localStorage.getItem('homeViewMode')
  if (savedViewMode) {
    viewMode.value = savedViewMode
  }
  
  // 请求素材库列表
  fetchLibraries()
})
</script>

<style scoped>
</style>
