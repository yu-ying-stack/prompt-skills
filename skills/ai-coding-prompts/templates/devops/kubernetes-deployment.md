# Kubernetes 部署策略 Prompt 模板

## 元信息

| 字段 | 值 |
| ------ | ----- |
| 模板ID | DEVOPS-K8S-003 |
| 版本 | 1.0 |
| 分类 | DevOps与部署 / Kubernetes |
| 适用场景 | Kubernetes 上线、弹性伸缩、灰度发布、配置治理、工作负载安全 |
| 创建日期 | 2026-06-08 |
| 作者 | AI Coding Prompt 模板库 |

## 角色定位

你是一位资深云原生平台工程师，拥有 10 年以上 Kubernetes 生产运维经验，精通 Deployment、StatefulSet、Ingress、HPA、ConfigMap、Secret、Service Mesh 与发布治理。

## 输入参数

| 参数名 | 类型 | 必填 | 说明 |
| -------- | ------ | ------ | ------ |
| WORKLOAD_TYPE | String | 是 | 工作负载类型，如 Web 服务、状态服务、后台任务 |
| DEPLOY_ENV | String | 是 | 部署环境，如 dev、staging、prod |
| TRAFFIC_STRATEGY | String | 是 | 流量策略，如 蓝绿、金丝雀、滚动发布 |
| RESOURCE_PROFILE | String | 是 | CPU、内存、伸缩和副本要求 |
| CONFIG_REQUIREMENTS | String | 是 | 配置、密钥、持久化、网络策略要求 |
| OBSERVABILITY_REQUIREMENTS | String | 否 | 日志、指标、探针、告警要求 |

## Prompt 正文

请基于以下信息，设计一套 Kubernetes 部署方案，并输出完整清单与治理建议。

**工作负载类型：** {{WORKLOAD_TYPE}}
**部署环境：** {{DEPLOY_ENV}}
**流量策略：** {{TRAFFIC_STRATEGY}}
**资源画像：** {{RESOURCE_PROFILE}}
**配置要求：** {{CONFIG_REQUIREMENTS}}
**可观测性要求：** {{OBSERVABILITY_REQUIREMENTS}}

请完成以下任务：

1. 选择合适的 Kubernetes 资源对象并说明原因。
2. 给出 Deployment 或 StatefulSet、Service、Ingress、HPA、ConfigMap、Secret 等 YAML 示例。
3. 说明发布策略、回滚策略、资源限制、探针配置和节点调度规则。
4. 说明配置变更、密钥管理、网络隔离和租户隔离方案。
5. 给出运维风险、容量规划和故障演练建议。

## 约束条件

1. 必须明确工作负载类型与资源对象映射关系，不得混用不适合的控制器。
2. 必须配置就绪探针、存活探针和资源 requests/limits，禁止使用无约束部署。
3. 必须将敏感配置放入 Secret，并说明加密与访问控制策略，不得在 YAML 中明文写密钥。
4. 必须定义发布与回滚流程，禁止直接在生产环境进行不可回退的变更。
5. 必须说明网络策略、服务暴露和最小权限原则，不得默认开放全部访问路径。

## 输出要求

1. 输出 Kubernetes 架构说明与资源清单。
2. 输出核心 YAML 配置示例。
3. 输出发布、回滚、弹性伸缩与容量治理方案。
4. 输出安全、网络与配置治理建议。
5. 输出风险项与排障指引。

6. 至少输出 1 个矩阵表、1 个流程图（可用 Mermaid 或等价文本流程）和 1 个风险清单（含风险、影响、缓解措施）。

## 输出格式

```markdown
# Kubernetes 部署方案

## 1. 架构与资源规划

## 2. 资源清单

| 资源类型 | 名称 | 作用 |
| ---------- | ------ | ------ |`r`n`r`n## 3. YAML 示例

    # kubernetes manifests

## 4. 发布与回滚策略

## 5. 安全与可观测性治理

## 6. 风险与运维建议

## 附录 A. 发布与控制矩阵

| 环节 | 关键输入 | 控制点 | 产出 |
| ------ | ------ | ------ | ------ |

## 附录 B. 流程图

（使用 Mermaid 或等价文本流程，至少包含：变更提交 -> 质量门禁 -> 部署执行 -> 结果验证 -> 回滚或放量）

## 附录 C. 风险清单

| 风险 | 触发条件 | 影响 | 缓解措施 | 回退方式 |
| ------ | ------ | ------ | ------ | ------ |

## 自检清单

- [ ] 是否选择了正确的 Kubernetes 资源对象
- [ ] 是否配置了探针、资源限制和伸缩策略
- [ ] 是否说明了 Secret、网络策略和权限控制
- [ ] 是否定义了发布与回滚机制
- [ ] 是否给出了可执行的 YAML 示例
