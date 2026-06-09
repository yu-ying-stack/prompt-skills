---
title: 视觉设计稿转 Vue 3 项目骨架
summary: 将单张设计稿或多页设计转换为 Vue 3 + Vite + TypeScript 项目结构与关键组件代码
author: ai-coding-prompts team
tags:
  - visual-to-code
  - vue
  - codegen
inputs:
  - name: images
    type: files
    description: 用户上传的图像文件（截图、手绘、Figma 导出）
  - name: target
    type: string
    description: 目标技术栈（默认：Vue 3 + Vite + TypeScript + Element Plus）
    required: false
  - name: constraints
    type: string
    description: 用户额外约束（响应式、支持暗黑模式、只生成单页面等）
    required: false
---

## 元信息

- 版本：0.1
- 预期输出：项目文件树、关键配置文件、部分组件源码、样式 Token、可运行说明、自检报告

## 输入参数

- `{{images}}`：上传的图片集合
- `{{target}}`：目标栈（可选）
- `{{constraints}}`：额外约束（可选）

## Prompt 正文

请将以下内容作为模板使用：

1. 执行视觉结构化解析（Stage 1），输出 Visual IR（JSON），严格遵守约定的 schema。
2. 基于 Visual IR 执行组件映射（Stage 2），将视觉元素映射到 Element Plus 或自定义组件，输出增强 IR。
3. 推断布局与响应式策略（Stage 3），输出 DOM 树与 CSS 布局建议。
4. 生成项目骨架和关键组件代码（Stage 4），按文件清单输出可复制的代码块。
5. 运行自检清单（Stage 5），输出自检报告并列出 TODO/不确定项。

输出要求：

- 必须输出 JSON 格式的 Visual IR（Stage 1）
- 必须输出增强 IR 与组件映射表（Stage 2）
- 必须输出项目文件树与至少 3 个关键组件源码（Stage 4）
- 必须包含自检报告，说明未决项和建议（Stage 5）

## 附录

Appendix A: 输出文件清单模板

Appendix B: 自检报告模板

Appendix C: 设计 Token 示例
