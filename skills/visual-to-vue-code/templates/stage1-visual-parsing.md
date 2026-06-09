---
title: Stage1 - 视觉结构化解析（Visual Parsing）
summary: 将上传的图片解析为严格的 Visual IR（JSON），用于后续组件映射与布局还原
tags:
  - stage1
  - visual-ir
inputs:
  - name: images
    type: files
  - name: instruction
    type: string
---

## 要求

- 请严格输出 JSON 格式的 Visual IR，遵守以下 schema（meta/layout/components/dataFlows）。
- 必须附带 `confidence` 字段；当识别低置信度时，标注 `"note": "低置信度，需人工确认"`。
- 必须输出识别思路（简短链路推理，最多 6 行）。

## 输出示例（部分）

```json
{
  "meta": {"imageType": "ui-screenshot", "confidence": "high", "pageType": "dashboard"},
  "layout": {"structure": "sidebar-main", "regions": [{"id":"r1","role":"sidebar","position":"left","approxSize":"narrow"}]},
  "components": [{"id":"c1","visualType":"button","mappedComponent":"el-button","regionId":"r2","content":{"text":"查询"}}],
  "dataFlows": []
}
```
