---
id: visual-to-vue-code
name: visual-to-vue-code
version: 0.1.0
display_name: 视觉设计稿转 Vue 3 代码
author: DevTeam
license: MIT
description: |
  将用户上传的视觉设计（截图、手绘草图、Figma 导出）转换为可运行的 Vue 3 + Vite + TypeScript 项目骨架与组件代码。
tags:
  - frontend
  - vue
  - multimodal
  - codegen
  - visual-to-code
triggers:
  - "转成 Vue 代码"
  - "生成前端页面"
  - "根据这张图写代码"
  - "实现这个界面"
  - "视觉转代码"
examples:
  - examples/example-visual-to-vue-1.md
roles:
  - author: AI assistant
  - maintainer: repo owner
---

## 概述

此 Skill 基于 repository 中的 `skills/ai-coding-prompts` 规范构建，遵循已制定的元信息、输入参数与 Prompt 模板格式。核心能力为将图片与用户指令转为五阶段流水线的可执行输出：视觉结构化解析 → 组件映射 → 布局还原 → 工程化代码生成 → 自检与交付。

## 使用说明

- 输入：一张或多张图片（UI 设计稿、手绘草图、Figma 导出图）与自然语言指令
- 输出：包含项目文件树、关键文件（package.json、vite 配置、src 代码文件）、组件与样式、以及自检报告的可复制代码块

## 模板位置

本 Skill 的 Prompt 模板保存在 `templates/`，示例在 `examples/`，实现细节与约束在 `references/visual-to-vue-code.md`。

## 发布准备检查清单

- [ ] Frontmatter 校验通过（`id/name` 符合规范，`examples` 路径存在）
- [ ] 模板（`templates/`）与示例（`examples/`）覆盖 Stage1–Stage5
- [ ] references 中包含技术方案与约束（已引用 `docs/visual-to-vue-code-skill.md`）
- [ ] README/索引已在 `skills/ai-coding-prompts` 中互链
- [ ] 运行 `get_errors` 无 Markdown/YAML 报错
- [ ] 提交变更（建议 commit 信息："add visual-to-vue-code skill and templates"）

发布流程建议：

1. 在 feature 分支上完成变更并本地校验（`get_errors`）
2. 提交并发起 PR，PR 描述中引用本 Skill 的用途与约束
3. 由 repo owner 审核并合并到主分支
4. 在发布说明中加入使用示例与快速开始

