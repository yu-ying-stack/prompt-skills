# 从代码生成 OpenAPI 文档模板
## 元信息
- 场景: 根据控制器/路由注释生成 OpenAPI 规范草稿
## 输入参数
- `language_framework`: 代码语言与框架
- `routes`: 路由清单或控制器代码片段
## Prompt 正文
请基于提供的路由和参数示例生成 OpenAPI 3.0 YML/JSON，并标注必填字段、响应示例和错误码。
