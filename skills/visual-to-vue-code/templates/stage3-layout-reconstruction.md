---
title: Stage3 - 布局还原（Layout Reconstruction）
summary: 根据增强 IR 推断 DOM 树与 CSS 布局策略（Flex / Grid / Container 选择）
tags:
  - stage3
inputs:
  - name: enhanced_ir
    type: json
---

## 要求

- 输出 DOM 树（JSON）示例，标注容器类型（el-container / el-row / el-col / grid）和响应式断点策略。
- 提供每个主要容器的 CSS 建议（flex/grid 样式与关键 media queries）。
