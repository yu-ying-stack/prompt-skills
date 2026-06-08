# 示例：使用监控与告警设计模板

## 场景描述

为支付服务设计业务可用性和错误率告警，要求支持 SLO 和 on-call 升级机制。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| SYSTEM_SCOPE | 支付服务、支付网关和回调处理链路 |
| BUSINESS_OBJECTIVES | 支付成功率稳定、支付超时可快速发现、异常订单可追踪 |
| OBSERVABILITY_STACK | Prometheus、Alertmanager、Grafana、Tempo |
| ALERTING_RULES | 支付成功率低于 99.5%、P95 延迟超过 800ms、错误率高于 1% 时告警 |
| ONCALL_MODEL | 工作日主值班 + 备值班，P1 5 分钟内响应，15 分钟内升级 |
| SLO_TARGETS | 月度可用性 99.95%，核心交易链路错误预算按月管理 |

## 可直接使用的 Prompt

请基于以下信息，设计一套监控与告警体系，兼顾业务价值、可操作性和噪音控制。

**系统范围：** {{SYSTEM_SCOPE}}
**业务目标：** {{BUSINESS_OBJECTIVES}}
**可观测性栈：** {{OBSERVABILITY_STACK}}
**告警要求：** {{ALERTING_RULES}}
**值班模式：** {{ONCALL_MODEL}}
**SLO 目标：** {{SLO_TARGETS}}

请输出 SLI/SLO、告警规则、Runbook 和降噪策略。