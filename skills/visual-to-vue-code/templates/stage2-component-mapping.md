---
title: Stage2 - 组件映射与标准化（Component Mapping）
summary: 将 Visual IR 中的视觉元素映射为 Element Plus 或自定义组件，并输出增强 IR
tags:
  - stage2
  - mapping
inputs:
  - name: visual_ir
    type: json
---

## 要求

- 使用本仓库约定的组件映射表，将 `visualType` 映射到 `mappedComponent`。
- 输出增强 IR，包含 `props`、`events`、`dataBindings` 字段。
- 对每个无法直接映射的视觉类型，生成 `CustomXxx` 命名建议并说明降级实现。
