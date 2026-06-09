---
title: Stage5 - 自检与交付（Self-Review & Delivery）
summary: 输出自检报告并列出 TODO/不确定项，确认可运行性检查步骤
tags:
  - stage5
inputs:
  - name: generated_project
    type: string
---

## 自检清单

- 视觉完整性：图中元素映射覆盖率
- 组件正确性：组件映射与 props/events 检查
- 布局准确性：DOM 嵌套与布局声明一致
- 类型安全：TS 类型声明检查
- 运行性：提供 `npm install` 与 `npm run dev` 的检查建议

## 输出要求

- 输出一份 Markdown 格式的自检报告，包含复选项与未解决的 TODO 列表。
