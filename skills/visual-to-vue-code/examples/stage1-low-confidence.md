# Stage1 示例 - 低置信度（手绘草图）

输入说明：用户上传一张手绘草图，线条粗糙，部分文本难以辨认。

用户指令："请根据手绘草图推断 Visual IR，并标注需人工确认的字段。"

期望输出（摘要）：

```json
{
  "meta": {"imageType": "hand-drawn-sketch", "confidence": "low", "pageType": "form-page"},
  "layout": {"structure": "topnav-main", "regions": [{"id":"r1","role":"header"},{"id":"r2","role":"main"}]},
  "components": [
    {"id":"c1","visualType":"text-block","mappedComponent":"div","regionId":"r2","content":{"text":"<需要确认>"}},
    {"id":"c2","visualType":"input","mappedComponent":"el-input","regionId":"r2","content":{"placeholder":"<需要确认>"}}
  ],
  "note": "低置信度，文本与部分布局需人工确认"
}
```

需人工确认项：文本字段内容、表单字段顺序。
