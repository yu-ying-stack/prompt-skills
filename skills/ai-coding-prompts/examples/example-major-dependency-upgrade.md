# 示例：使用主要依赖升级模板

## 场景描述

将一个使用 Spring Boot 2.7 的平台服务升级到 Spring Boot 3.5，并评估 Jakarta 迁移影响。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| DEPENDENCY_SCOPE | Spring Boot 2.7、Spring Security 5、Hibernate 5 |
| TARGET_VERSION | Spring Boot 3.5、Spring Security 6、Hibernate 6 |
| CODEBASE_CONTEXT | 多模块 Maven 项目，包含 REST API、批处理任务和 OAuth2 认证 |
| BREAKING_CHANGES | Jakarta 包名迁移、Security 配置 API 变化、Hibernate 查询兼容性变化 |
| VALIDATION_REQUIREMENTS | 编译通过、单元测试、集成测试、灰度环境验证、失败可快速回滚 |
| RELEASE_CONSTRAINTS | 两个版本窗口完成升级，不能中断对外 API 服务 |

## 可直接使用的 Prompt

请基于以下信息，制定一套主要依赖升级方案，并输出风险、改造步骤和验证计划。

**升级范围：** {{DEPENDENCY_SCOPE}}
**目标版本：** {{TARGET_VERSION}}
**代码库上下文：** {{CODEBASE_CONTEXT}}
**破坏性变更：** {{BREAKING_CHANGES}}
**验证要求：** {{VALIDATION_REQUIREMENTS}}
**发布约束：** {{RELEASE_CONSTRAINTS}}

请重点说明 Jakarta 迁移、阶段化改造和灰度回滚策略。