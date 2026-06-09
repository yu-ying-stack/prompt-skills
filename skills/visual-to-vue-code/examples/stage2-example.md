# Stage2 示例 - 组件映射示例

输入：Stage1 输出的 Visual IR（示例见 `stage1-high-confidence.md`）

用户指令："请将 Visual IR 中的视觉元素映射到 Element Plus 组件，并输出增强 IR（包含 props/events/dataBindings）。"

期望输出（摘要）：

```json
{
  "components": [
    {"id":"c2","mappedComponent":"el-table","props":{"columns":["id","name","status","updatedAt"]},"events":{"onSort":"handleSort","onPageChange":"handlePage"}},
    {"id":"c3","mappedComponent":"el-button","props":{"type":"primary","size":"default"},"events":{"onClick":"handleAdd"}}
  ]
}
```

降级说明：若某图标无法识别，建议生成 `CustomIconX.vue` 并使用占位 SVG。
