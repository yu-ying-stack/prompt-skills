# TypeScript 迁移策略模板
---
元信息:
	模板名称: typescript-migration
	模板类型: refactoring
	适用场景: 从 JavaScript 迁移到 TypeScript 的分阶段计划与风险评估
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 从 JavaScript 迁移到 TypeScript 的分阶段计划与风险评估

## 输入参数
- `codebase_size`: 代码库规模估算
- `priority_modules`: 优先迁移模块

## Prompt 正文
输出分阶段迁移计划、必要的 tsconfig、逐步引入策略（any->unknown->strict）和回滚策略。
