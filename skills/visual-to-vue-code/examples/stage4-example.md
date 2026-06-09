# Stage4 示例 - 工程化代码生成示例

输入：DOM 树 + 组件映射

用户指令："生成项目的关键文件（package.json、src/main.ts、src/App.vue、components/DataTable.vue）。"

期望输出（摘要）：

1. `package.json`（见 `templates/stage4-samples.md`）
2. `src/main.ts` 示例代码
3. `src/components/DataTable.vue` 示例（简化）

示例 DataTable（摘要）：

```vue
<template>
  <el-table :data="rows">
    <el-table-column prop="id" label="ID"/>
    <el-table-column prop="name" label="Name"/>
  </el-table>
  </el-table>
</template>
```
