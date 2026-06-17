# 从代码生成 OpenAPI 文档模板
---
元信息:
	模板名称: openapi-from-code
	模板类型: code-generation
	适用场景: 根据控制器/路由注释生成 OpenAPI 规范草稿
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 根据控制器/路由注释生成 OpenAPI 规范草稿

## 输入参数
- `language_framework`: 代码语言与框架
- `routes`: 路由清单或控制器代码片段

## Prompt 正文
请基于提供的路由和参数示例生成 OpenAPI 3.0 YML/JSON，并标注必填字段、响应示例和错误码。

## 输出要求
- 提供完整的 OpenAPI 3.0 文档（YAML/JSON）示例
- 标注每个路径的参数、响应示例与可能的错误码
- 给出如何从代码注释/注解生成文档的步骤与示例命令（例如 swagger-jsdoc、springdoc）

## 自检清单
- 是否生成了有效的 OpenAPI 文档片段
- 是否包含响应示例与错误码说明
- 是否包含从代码生成的实用指南或命令示例
