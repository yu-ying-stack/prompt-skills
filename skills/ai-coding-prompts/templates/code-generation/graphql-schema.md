# GraphQL Schema 生成模板
---
元信息:
	模板名称: graphql-schema
	模板类型: code-generation
	适用场景: 根据用例生成 GraphQL schema 与 resolver 骨架
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 根据用例生成 GraphQL schema 与 resolver 骨架

## 输入参数
- `entities`: 实体定义（字段、类型、关联）
- `auth`: 是否包含权限字段

## Prompt 正文
生成可运行的 GraphQL SDL，包含查询/变更/分页/输入类型与 resolver 注释，说明如何映射到后端数据源。

## 输出要求
- 完整 GraphQL SDL 示例（schema.graphql）
- 对应 resolver 的代码骨架（根据指定语言示例：Node/Java/Go）
- 示例查询、变更、分页实现示例与访问控制注释
- 映射到数据库表/ORM 的示例说明

## 自检清单
- SDL 是否包含查询/变更/分页/输入类型
- Resolver 骨架是否含有注释和示例映射点
- 是否提供示例权限字段与访问控制策略
