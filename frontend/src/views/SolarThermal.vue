<template>
  <div class="solar-thermal-container">
    <!-- 工具栏 -->
    <div class="toolbar">
      <el-card shadow="hover">
        <div class="toolbar-content">
          <div class="toolbar-left">
            <div class="logo">
              <el-icon size="24"><Sunrise /></el-icon>
              <span class="logo-text">光热电厂监控系统</span>
            </div>
            <div class="nav-menu">
              <router-link to="/" class="nav-item">总体预览</router-link>
              <router-link to="/fault-alarm" class="nav-item">故障告警</router-link>
              <router-link to="/solar-thermal" class="nav-item active">光热电厂</router-link>
            </div>
          </div>
          <div class="toolbar-right">
            <el-button type="primary" :icon="Refresh" @click="refreshData">
              刷新数据
            </el-button>
            <el-button :icon="Setting" @click="navigateToSettings">
              系统设置
            </el-button>
          </div>
        </div>
      </el-card>
    </div>

    <!-- 主要内容区域 -->
    <div class="main-content">
      <!-- 2 列 3 行布局 -->
      <div class="charts-grid">
        <!-- 第一行第一列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>发电功率趋势</span>
              </div>
            </template>
            <div ref="powerChart" class="echart-container"></div>
          </el-card>
        </div>

        <!-- 第一行第二列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>太阳辐射强度</span>
              </div>
            </template>
            <div ref="radiationChart" class="echart-container"></div>
          </el-card>
        </div>

        <!-- 第二行第一列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>储热罐温度分布</span>
              </div>
            </template>
            <div ref="temperatureChart" class="echart-container"></div>
          </el-card>
        </div>

        <!-- 第二行第二列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>蒸汽流量监测</span>
              </div>
            </template>
            <div ref="steamFlowChart" class="echart-container"></div>
          </el-card>
        </div>

        <!-- 第三行第一列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>汽轮机效率分析</span>
              </div>
            </template>
            <div ref="turbineEfficiencyChart" class="echart-container"></div>
          </el-card>
        </div>

        <!-- 第三行第二列 -->
        <div class="chart-item">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <span>日发电量统计</span>
              </div>
            </template>
            <div ref="dailyGenerationChart" class="echart-container"></div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { Refresh, Setting, Sunrise } from '@element-plus/icons-vue'
import * as echarts from 'echarts'

const router = useRouter()
const powerChart = ref(null)
const radiationChart = ref(null)
const temperatureChart = ref(null)
const steamFlowChart = ref(null)
const turbineEfficiencyChart = ref(null)
const dailyGenerationChart = ref(null)

let chartInstances = []

// 导航到设置页面
const navigateToSettings = () => {
  router.push('/settings')
}

// 刷新数据
const refreshData = () => {
  initCharts()
}

// 初始化所有图表
const initCharts = () => {
  initPowerChart()
  initRadiationChart()
  initTemperatureChart()
  initSteamFlowChart()
  initTurbineEfficiencyChart()
  initDailyGenerationChart()
}

// 发电功率趋势图
const initPowerChart = () => {
  if (!powerChart.value) return
  
  const chart = echarts.init(powerChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['实际功率', '额定功率'],
      textStyle: {
        color: '#fff'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: 'MW',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '实际功率',
        type: 'line',
        smooth: true,
        data: [0, 0, 45, 120, 95, 0],
        itemStyle: {
          color: '#4FC3F7'
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(79, 195, 247, 0.5)' },
            { offset: 1, color: 'rgba(79, 195, 247, 0.1)' }
          ])
        }
      },
      {
        name: '额定功率',
        type: 'line',
        smooth: true,
        data: [0, 0, 100, 150, 150, 0],
        itemStyle: {
          color: '#FFB74D'
        },
        lineStyle: {
          type: 'dashed'
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 太阳辐射强度图
const initRadiationChart = () => {
  if (!radiationChart.value) return
  
  const chart = echarts.init(radiationChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: 'W/m²',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '辐射强度',
        type: 'line',
        smooth: true,
        data: [50, 280, 650, 920, 850, 520, 120],
        itemStyle: {
          color: '#FFA726'
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(255, 167, 38, 0.5)' },
            { offset: 1, color: 'rgba(255, 167, 38, 0.1)' }
          ])
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 储热罐温度分布图
const initTemperatureChart = () => {
  if (!temperatureChart.value) return
  
  const chart = echarts.init(temperatureChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ['冷罐', '热罐'],
      textStyle: {
        color: '#fff'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['1#罐', '2#罐', '3#罐', '4#罐'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: '°C',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '冷罐',
        type: 'bar',
        data: [280, 275, 285, 278],
        itemStyle: {
          color: '#42A5F5'
        }
      },
      {
        name: '热罐',
        type: 'bar',
        data: [565, 570, 560, 568],
        itemStyle: {
          color: '#EF5350'
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 蒸汽流量监测图
const initSteamFlowChart = () => {
  if (!steamFlowChart.value) return
  
  const chart = echarts.init(steamFlowChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['主蒸汽流量', '给水流量'],
      textStyle: {
        color: '#fff'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: 't/h',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '主蒸汽流量',
        type: 'line',
        smooth: true,
        data: [0, 0, 180, 320, 290, 0],
        itemStyle: {
          color: '#26C6DA'
        }
      },
      {
        name: '给水流量',
        type: 'line',
        smooth: true,
        data: [0, 0, 185, 325, 295, 0],
        itemStyle: {
          color: '#9575CD'
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 汽轮机效率分析图
const initTurbineEfficiencyChart = () => {
  if (!turbineEfficiencyChart.value) return
  
  const chart = echarts.init(turbineEfficiencyChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ['设计效率', '实际效率'],
      textStyle: {
        color: '#fff'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['25%', '50%', '75%', '100%'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: '%',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '设计效率',
        type: 'bar',
        data: [32, 38, 42, 45],
        itemStyle: {
          color: '#78909C'
        }
      },
      {
        name: '实际效率',
        type: 'bar',
        data: [30, 36, 40, 43],
        itemStyle: {
          color: '#66BB6A'
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 日发电量统计图
const initDailyGenerationChart = () => {
  if (!dailyGenerationChart.value) return
  
  const chart = echarts.init(dailyGenerationChart.value)
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      }
    },
    yAxis: {
      type: 'value',
      name: 'MWh',
      axisLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        }
      },
      axisLabel: {
        color: '#fff'
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.1)'
        }
      }
    },
    series: [
      {
        name: '发电量',
        type: 'bar',
        barWidth: '40%',
        data: [1250, 1380, 1420, 1350, 1480, 1520, 1450],
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#FFA726' },
            { offset: 1, color: '#FB8C00' }
          ])
        }
      }
    ]
  }
  chart.setOption(option)
  chartInstances.push(chart)
}

// 窗口大小改变时重新渲染图表
const handleResize = () => {
  chartInstances.forEach(chart => {
    chart.resize()
  })
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  // 等待 DOM 渲染完成后初始化图表
  setTimeout(() => {
    initCharts()
  }, 100)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  chartInstances.forEach(chart => {
    chart.dispose()
  })
  chartInstances = []
})
</script>

<style scoped>
.solar-thermal-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.toolbar {
  margin-bottom: 20px;
}

.toolbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: 30px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 20px;
  font-weight: bold;
}

.nav-menu {
  display: flex;
  gap: 20px;
}

.nav-item {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 4px;
  transition: all 0.3s;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-item.active {
  background: rgba(79, 195, 247, 0.3);
  color: white;
}

.toolbar-right {
  display: flex;
  gap: 10px;
  align-items: center;
}

.main-content {
  flex: 1;
  overflow: hidden;
}

.charts-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 20px;
  height: 100%;
}

.chart-item {
  height: 100%;
  min-height: 0;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  font-weight: bold;
}

.echart-container {
  width: 100%;
  height: calc(100% - 50px);
  min-height: 200px;
}
</style>
