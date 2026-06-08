# 示例：使用需求分析模板

## 场景描述

分析一个“企业管理员批量导入员工并自动分配组织结构”的需求，输出范围、风险和验收标准。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| BUSINESS_REQUEST | 企业管理员上传 Excel 批量导入员工，按部门编码自动归属组织，并向员工发送入职通知 |
| TARGET_USERS | 企业管理员、人力运营、被导入员工 |
| BUSINESS_RULES | 邮箱唯一、部门编码必须存在、重复导入需跳过并输出失败原因 |
| SYSTEM_CONTEXT | 企业管理后台、组织服务、通知服务、账号服务 |
| DELIVERY_CONSTRAINTS | 两个迭代上线，需符合审计要求并保留导入日志 |
| OPEN_QUESTIONS | 导入模板是否支持自定义字段，失败重试是否支持部分重跑 |

## 可直接使用的 Prompt

请基于以下信息，完成一份结构化需求分析，澄清范围、约束和验收标准。

**原始业务诉求：** {{BUSINESS_REQUEST}}
**目标用户：** {{TARGET_USERS}}
**业务规则：** {{BUSINESS_RULES}}
**系统上下文：** {{SYSTEM_CONTEXT}}
**交付约束：** {{DELIVERY_CONSTRAINTS}}
**未决问题：** {{OPEN_QUESTIONS}}

请输出范围边界、待确认问题、验收标准和交付风险。