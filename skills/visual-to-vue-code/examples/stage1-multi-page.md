# Stage1 示例 - 多页设计（多页面/路由）

输入说明：用户上传多张页面截图，代表同一产品的不同页面（列表页、详情页、编辑页），希望识别页面间导航关系并生成路由映射。

用户指令："请根据上传的多张截图生成 Visual IR，识别页面间的跳转关系并输出 pageId 和 route 建议。"

期望输出（摘要）：

```json
{
  "meta": {"imageType": "ui-screenshot", "confidence": "high", "pageType": "mixed"},
  "pages": [
    {"pageId":"p_list","title":"列表页","regions":[{"id":"r1","role":"main"}]},
    {"pageId":"p_detail","title":"详情页","regions":[{"id":"r2","role":"main"}]}
  ],
  "routes": [
    {"from":"p_list","to":"p_detail","trigger":"rowClick","route":"/items/:id"}
  ]
}
```

Chain-of-Thought（简短）:
1. 列表页表格通常包含操作列，点击行跳转到详情页，推断 route 模板为 `/items/:id`。
2. 详情页存在返回按钮，说明双向导航关系。
