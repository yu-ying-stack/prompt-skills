# Stage3 示例 - 响应式网格/卡片布局

输入：图中包含多列卡片（商品/概览卡片），需在不同断点切换列数。

用户指令："生成 DOM 树与 CSS Grid 建议，包含 1920px / 1366px / 768px 的行为说明。"

期望输出（摘要）：

```json
{
  "domTree": {"type":"div.grid","props":{"columnsDesktop":4,"columnsLaptop":3,"columnsMobile":1}},
  "css": {
    "grid": "display:grid;grid-template-columns:repeat(4,1fr);gap:16px;",
    "media": "@media (max-width:1366px){grid-template-columns:repeat(3,1fr);} @media (max-width:768px){grid-template-columns:repeat(1,1fr);}"
  }
}
```
