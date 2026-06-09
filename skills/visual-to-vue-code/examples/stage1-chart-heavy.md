# Stage1 示例 - 图表密集型页面

输入说明：上传包含多个图表（折线、柱状、饼图）的仪表盘截图。

用户指令："识别图表区域并为每个图表生成推荐的图表类型与数据字段映射。"

期望输出（摘要）：

```json
{
  "components": [
    {"id":"c1","visualType":"chart","mappedComponent":"custom-chart","content":{"chartType":"line","suggestedDataKeys":["date","value"]}},
    {"id":"c2","visualType":"chart","mappedComponent":"custom-chart","content":{"chartType":"bar","suggestedDataKeys":["category","count"]}}
  ]
}
```

注意：为图表生成 mock 数据示例，并在 Stage4 提供 ECharts 集成注释。
