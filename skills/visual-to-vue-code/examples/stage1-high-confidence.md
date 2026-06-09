# Stage1 示例 - 高置信度（单页仪表盘截图）

输入说明：用户上传一张清晰的仪表盘截图，包含顶部导航、左侧侧栏和主内容区表格与“新增”按钮。

用户指令："请根据上传的截图生成 Visual IR（JSON），并说明识别思路。"

期望输出（摘要）：

```json
{
  "meta": {"imageType": "ui-screenshot", "confidence": "high", "pageType": "dashboard"},
  "layout": {"structure": "sidebar-main", "regions": [{"id":"r1","role":"sidebar"},{"id":"r2","role":"main"}]},
  "components": [
    {"id":"c1","visualType":"topnav","mappedComponent":"AppHeader","regionId":"r2"},
    {"id":"c2","visualType":"table","mappedComponent":"el-table","regionId":"r2","content":{"columns":["id","name","status","updatedAt"]}},
    {"id":"c3","visualType":"button","mappedComponent":"el-button","regionId":"r2","content":{"text":"新增"}}
  ],
  "dataFlows": [{"source":"c3","target":"c2","type":"table-refresh"}]
}
```

识别思路（示例简短链路推理）：

1. 顶部长条样式识别为导航栏，映射为 `AppHeader`。
2. 左侧竖列为导航，识别为侧边栏 `AppSidebar`。
3. 主区中心的大表格识别为 `el-table`，右上角显著按钮识别为主操作按钮。
