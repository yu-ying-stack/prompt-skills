---
title: Stage4 - 工程化代码生成（Code Generation）
summary: 基于 DOM 树与组件映射生成可运行的 Vue 3 + Vite + TypeScript 项目文件与关键组件代码块
tags:
  - stage4
inputs:
  - name: dom_tree
    type: json
  - name: mapping
    type: json
---

## 要求

- 按清单输出项目文件树和关键文件的完整代码块（`package.json`、`vite.config.ts`、`src/main.ts`、`src/App.vue`、若干 `src/components/*.vue`）。
- 每个组件必须使用 `<script setup lang="ts">`、`scoped` 样式，并包含类型定义。
- 对外部依赖列出 `package.json` 的最小依赖集合。
