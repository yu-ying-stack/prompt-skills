# GraphQL Schema 生成模板
## 元信息
- 场景: 根据用例生成 GraphQL schema 与 resolver 骨架
## 输入参数
- `entities`: 实体定义（字段、类型、关联）
- `auth`: 是否包含权限字段
## Prompt 正文
生成可运行的 GraphQL SDL，包含查询/变更/分页/输入类型与 resolver 注释，说明如何映射到后端数据源。
