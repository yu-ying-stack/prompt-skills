# 示例输出：Visual IR（JSON）

```json
{
  "meta": {"imageType": "ui-screenshot", "confidence": "medium", "pageType": "dashboard"},
  "layout": {"structure": "sidebar-main", "regions": [{"id":"r1","role":"sidebar","position":"left","approxSize":"narrow"},{"id":"r2","role":"main","position":"center","approxSize":"large"}]},
  "components": [
    {"id":"c1","visualType":"topnav","mappedComponent":"AppHeader","regionId":"r2"},
    {"id":"c2","visualType":"table","mappedComponent":"el-table","regionId":"r2","content":{"columns":["id","name","status","updatedAt"]}},
    {"id":"c3","visualType":"button","mappedComponent":"el-button","regionId":"r2","content":{"text":"新增"}}
  ],
  "dataFlows": [{"source":"c3","target":"c2","type":"table-refresh"}]
}
```

注：`confidence` 为 `medium`，表明部分文字识别需人工确认。
