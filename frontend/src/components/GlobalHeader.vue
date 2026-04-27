<template>
  <div class="toolbar">
    <el-card shadow="hover">
      <div class="toolbar-content">
        <div class="toolbar-left">
          <div class="logo">
            <el-icon size="24"><WindPower /></el-icon>
            <span class="logo-text">风电智能监控平台</span>
          </div>
          <div class="nav-menu">
            <router-link to="/" class="nav-item" :class="{ active: activePage === 'dashboard' }">总体预览</router-link>
            <router-link to="/fault-alarm" class="nav-item" :class="{ active: activePage === 'fault-alarm' }">故障告警</router-link>
            <router-link to="/solar-thermal" class="nav-item" :class="{ active: activePage === 'solar-thermal' }">光热电厂</router-link>
            <router-link v-if="showSettingsNav" to="/settings" class="nav-item" :class="{ active: activePage === 'settings' }">系统设置</router-link>
            <router-link v-if="showAnalysisNav" to="/analysis" class="nav-item" :class="{ active: activePage === 'analysis' }">分析页面</router-link>
            <router-link v-if="showLocalAnalysisNav" to="/local-analysis" class="nav-item" :class="{ active: activePage === 'local-analysis' }">局部分析</router-link>
          </div>
        </div>

        <div class="toolbar-right">
          <el-button v-if="showRefresh" type="primary" :icon="Refresh" @click="$emit('refresh')">刷新数据</el-button>
          <el-button v-if="showSettingsButton" :icon="Setting" @click="$emit('open-settings')">系统设置</el-button>

          <el-select
            v-if="showTurbineSelect"
            v-model="selectedTurbine"
            placeholder="选择或输入风机编号（0-255）"
            clearable
            filterable
            allow-create
            default-first-option
            :reserve-keyword="false"
            @change="handleTurbineChange"
          >
            <el-option
              v-for="item in turbineOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { ElMessage } from 'element-plus'
import { Refresh, Setting, WindPower } from '@element-plus/icons-vue'

const props = defineProps({
  activePage: {
    type: String,
    default: 'dashboard'
  },
  modelValue: {
    type: String,
    default: ''
  },
  showRefresh: {
    type: Boolean,
    default: true
  },
  showSettingsButton: {
    type: Boolean,
    default: true
  },
  showTurbineSelect: {
    type: Boolean,
    default: true
  },
  showSettingsNav: {
    type: Boolean,
    default: false
  },
  showAnalysisNav: {
    type: Boolean,
    default: false
  },
  showLocalAnalysisNav: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'refresh', 'open-settings', 'turbine-change'])

const selectedTurbine = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const turbineOptions = Array.from({ length: 256 }, (_, index) => {
  const turbineId = `T${String(index).padStart(3, '0')}`
  return {
    label: `风机${index} (${turbineId})`,
    value: turbineId
  }
})

const normalizeTurbineId = (input) => {
  if (!input) {
    return null
  }

  const normalizedInput = String(input).trim().toUpperCase()
  const match = normalizedInput.match(/^T?(\d{1,3})$/)
  if (!match) {
    return null
  }

  const turbineNumber = Number(match[1])
  if (!Number.isInteger(turbineNumber) || turbineNumber < 0 || turbineNumber > 255) {
    return null
  }

  return `T${String(turbineNumber).padStart(3, '0')}`
}

const handleTurbineChange = (value) => {
  if (!value) {
    emit('update:modelValue', '')
    return
  }

  const normalizedId = normalizeTurbineId(value)
  if (!normalizedId) {
    ElMessage.warning('请输入 0-255 范围内的风机编号，例如 12 或 T012')
    emit('update:modelValue', '')
    return
  }

  emit('update:modelValue', normalizedId)
  emit('turbine-change', normalizedId)
}
</script>

<style scoped>
.toolbar {
  width: 100%;
  height: 60px;
  padding: 0 10px;
  margin-bottom: 15px;
  z-index: 3;
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
