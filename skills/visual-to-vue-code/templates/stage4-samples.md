---
title: Stage4 - 关键文件样例（package.json / vite.config / main / App.vue / components）
summary: 提供 Stage4 的可复制示例代码片段，便于生成器产出可运行项目
---

## package.json（最小依赖示例）

```json
{
  "name": "vt-sample",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "serve": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.0",
    "element-plus": "^2.4.0",
    "@element-plus/icons-vue": "^2.0.0",
    "pinia": "^2.0.0",
    "vue-router": "^4.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "typescript": "^5.0.0",
    "unplugin-vue-components": "^0.26.0",
    "unplugin-auto-import": "^0.14.0",
    "eslint": "^8.0.0",
    "prettier": "^2.0.0"
  }
}
```

## src/main.ts

```ts
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

createApp(App).use(ElementPlus).mount('#app')
```

## src/App.vue（简化）

```vue
<template>
  <el-container>
    <AppHeader />
    <el-main>
      <slot />
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
import AppHeader from '@/components/common/AppHeader.vue'
</script>

<style scoped lang="scss">
/* global layout styles */
</style>
```

## 组件示例：`AppHeader.vue`

```vue
<template>
  <header class="app-header">
    <div class="logo">MyApp</div>
    <el-menu mode="horizontal" class="nav">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">仪表盘</el-menu-item>
    </el-menu>
  </header>
</template>

<script setup lang="ts">
// props/types if needed
</script>

<style scoped lang="scss">
.app-header{display:flex;align-items:center;justify-content:space-between;padding:12px 24px}
</style>
```

## 组件示例：`DataTable.vue`（简化）

```vue
<template>
  <el-table :data="rows">
    <el-table-column prop="id" label="ID"/>
    <el-table-column prop="name" label="Name"/>
    <el-table-column prop="status" label="Status"/>
  </el-table>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const rows = ref([] as Array<Record<string, any>>)
</script>

<style scoped lang="scss">
</style>
```

## 设计 Token 示例（`src/styles/variables.css`）

```css
:root {
  --vt-primary-color: #409EFF;
  --vt-text-primary: #303133;
  --vt-space-md: 16px;
}
```
