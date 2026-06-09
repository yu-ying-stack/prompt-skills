# Stage3 示例 - 布局还原示例

输入：增强 IR（来自 Stage2）

用户指令："根据增强 IR 生成 DOM 树与 CSS 布局建议（包含 media queries）。"

期望输出（摘要）：

```json
{
  "domTree": {
    "type":"el-container",
    "children":[{"type":"el-aside","props":{"width":"220px"}},{"type":"el-main","children":[{"type":"AppHeader"},{"type":"DataTable"}]}]
  },
  "css": {
    "main": "display:flex;flex-direction:column;gap:16px;",
    "media": "@media (max-width:1366px){ .app-main{padding:8px} }"
  }
}
```
