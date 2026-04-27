<template>
  <div class="analysis-container">
    <GlobalHeader
      active-page="analysis"
      show-analysis-nav
      v-model="selectedTurbine"
      @refresh="refreshData"
      @open-settings="navigateToSettings"
      @turbine-change="navigateToTurbine"
    />

    <el-card class="page-title" shadow="hover">
      <h2>局部分析</h2>
      <p>这里将添加局部分析的具体内容</p>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import GlobalHeader from '@components/GlobalHeader.vue'

const router = useRouter()
const selectedTurbine = ref('')

const navigateToTurbine = (turbineIdInput) => {
  if (turbineIdInput) {
    router.push(`/local-analysis/${turbineIdInput}`)
  }
}

const navigateToSettings = () => {
  router.push('/settings')
}

const refreshData = () => {
  ElMessage.success('分析数据已刷新')
}
</script>

<style scoped>
.analysis-container {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 10px;
  background: rgba(39, 64, 139, 0.8);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
}

.toolbar {
  width: 100%;
  height: 60px;
  padding: 0 10px;
  margin-bottom: 15px;
}

.toolbar :deep(.el-card) {
  height: 100%;
  border-radius: 12px;
}

.toolbar-content {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 15px;
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  color: white;
}

.logo-text {
  font-size: 16px;
  font-weight: 600;
  color: white;
  text-shadow: 0 0 10px rgba(79, 195, 247, 0.7);
}

.nav-menu {
  display: flex;
  gap: 8px;
}

.nav-item {
  padding: 6px 12px;
  border-radius: 6px;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-size: 12px;
  font-weight: 500;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.nav-item:hover {
  background: rgba(79, 195, 247, 0.3);
  color: white;
  box-shadow: 0 0 10px rgba(79, 195, 247, 0.5);
}

.nav-item.active {
  background: rgba(79, 195, 247, 0.5);
  color: white;
  box-shadow: 0 0 15px rgba(79, 195, 247, 0.7);
  border-color: rgba(79, 195, 247, 0.8);
}

.toolbar-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.page-title {
  border-radius: 12px;
}

.page-title h2,
.page-title p {
  margin: 0;
  color: white;
}

.page-title p {
  margin-top: 12px;
  color: rgba(255, 255, 255, 0.8);
}

@media (max-width: 768px) {
  .toolbar {
    height: auto;
    padding: 0 5px;
  }

  .toolbar-content {
    flex-direction: column;
    gap: 10px;
    padding: 10px;
  }

  .toolbar-left {
    flex-direction: column;
    gap: 10px;
  }

  .toolbar-right {
    width: 100%;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>