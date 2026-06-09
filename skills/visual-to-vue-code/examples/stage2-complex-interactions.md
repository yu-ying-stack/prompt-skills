# Stage2 示例 - 复杂交互与数据绑定

输入：来自 Stage1 的增强 IR，包含表格、表单、筛选器、以及图表。

用户指令："为以下组件生成增强 IR，包含 props、events、dataBindings、以及建议的 API 端点（mock）。"

期望输出（摘要）：

```json
{
  "components": [
    {"id":"table1","mappedComponent":"DataTable","props":{"columns":["id","name","status"]},"events":{"onSearch":"handleSearch"},"dataBindings":{"fetch":"GET /api/items"}},
    {"id":"filter1","mappedComponent":"FilterPanel","events":{"onApply":"handleFilterApply"},"dataBindings":{"applyTo":"table1"}}
  ]
}
```

建议 API（mock）:

- `GET /api/items?page=1&pageSize=20&filter=status:active`
- `POST /api/items` (新增)
