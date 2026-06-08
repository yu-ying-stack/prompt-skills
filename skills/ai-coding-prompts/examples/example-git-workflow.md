# 示例：使用 Git 工作流设计模板

## 场景描述

为一个每周发布两次、使用 GitHub 和 Monorepo 的 20 人团队设计 Git 工作流。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| TEAM_MODEL | 20 人跨职能团队，前后端和 QA 共用 Monorepo，采用 PR 驱动协作 |
| RELEASE_CADENCE | 每周二、周五固定发布，支持紧急 hotfix |
| REPOSITORY_STRUCTURE | Monorepo |
| QUALITY_CONTROLS | main 分支必须通过 CI、双人审查、禁止直接 push |
| HOTFIX_REQUIREMENTS | 生产故障需 30 分钟内建立 hotfix 分支并支持快速回滚 |
| COMPLIANCE_RULES | 所有合并保留审计记录，关键分支仅发布管理员有写权限 |

## 可直接使用的 Prompt

请基于以下信息，设计一套 Git 工作流，并说明分支模型、合并策略和治理规则。

**团队模型：** {{TEAM_MODEL}}
**发布节奏：** {{RELEASE_CADENCE}}
**仓库结构：** {{REPOSITORY_STRUCTURE}}
**质量控制：** {{QUALITY_CONTROLS}}
**热修复要求：** {{HOTFIX_REQUIREMENTS}}
**合规规则：** {{COMPLIANCE_RULES}}

请重点输出分支生命周期、PR 门禁和 hotfix 流程。