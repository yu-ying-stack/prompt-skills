# 示例：使用 LLM 应用开发模板

## 场景描述

设计一个企业知识库问答助手，支持文档检索、工单查询和权限过滤。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| USE_CASE | 企业内部知识问答助手，覆盖制度文档、产品手册和工单 FAQ |
| MODEL_STACK | GPT-5.4 API、向量库、函数调用网关 |
| KNOWLEDGE_SOURCES | Confluence、PDF 文档、工单系统、内部 Wiki |
| TOOLING_INTEGRATIONS | 工单详情查询、用户权限校验、反馈收集接口 |
| SAFETY_REQUIREMENTS | 按用户部门控制文档可见性，禁止泄露敏感制度和客户信息 |
| EVALUATION_GOALS | 回答准确率、引用率、平均延迟和每次会话成本可量化 |

## 可直接使用的 Prompt

请基于以下信息，设计一套 LLM 应用方案，并输出架构、流程与治理建议。

**应用场景：** {{USE_CASE}}
**模型栈：** {{MODEL_STACK}}
**知识来源：** {{KNOWLEDGE_SOURCES}}
**工具集成：** {{TOOLING_INTEGRATIONS}}
**安全要求：** {{SAFETY_REQUIREMENTS}}
**评估目标：** {{EVALUATION_GOALS}}

请重点说明 RAG、权限过滤、模型评估和成本控制。