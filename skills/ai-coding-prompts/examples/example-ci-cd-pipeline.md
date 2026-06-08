# 示例：使用 CI/CD 流水线设计模板

## 场景描述

为一个 Node.js + React Monorepo 设计 GitHub Actions 流水线，要求支持测试门禁、镜像构建和分环境部署。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| PIPELINE_PLATFORM | GitHub Actions |
| PROJECT_STACK | Node.js 22、pnpm workspace、React、NestJS、Docker |
| DELIVERY_STAGES | lint、unit test、integration test、build、docker scan、deploy |
| DEPLOY_ENVIRONMENTS | dev、staging、prod |
| QUALITY_GATES | 覆盖率不低于 80%、高危漏洞为 0、main 分支必须双审 |
| SECURITY_REQUIREMENTS | 使用 GitHub OIDC 获取云凭证，镜像必须签名并保留审计记录 |

## 可直接使用的 Prompt

请基于以下信息，设计一套可落地的 CI/CD 流水线方案，并输出可执行配置与实施建议。

**流水线平台：** {{PIPELINE_PLATFORM}}
**项目技术栈：** {{PROJECT_STACK}}
**流水线阶段：** {{DELIVERY_STAGES}}
**部署环境：** {{DEPLOY_ENVIRONMENTS}}
**质量门禁：** {{QUALITY_GATES}}
**安全要求：** {{SECURITY_REQUIREMENTS}}

请重点说明 Monorepo 缓存、矩阵构建、镜像制品管理和生产审批流设计。