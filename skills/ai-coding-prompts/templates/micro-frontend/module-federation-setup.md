# Module Federation 配置 Prompt 模板

## 元信息

| 字段 | 值 |
| ------ | ----- |
| 模板ID | MFE-MF-002 |
| 版本 | 1.0 |
| 分类 | 微前端 / Module Federation |
| 适用场景 | Webpack 或 Rspack Module Federation 配置、共享依赖治理 |
| 创建日期 | 2026-06-08 |
| 作者 | AI Coding Prompt 模板库 |

## 角色定位

你是一位资深前端平台工程师，精通 Webpack、Rspack 和 Module Federation，擅长设计 Host/Remote 架构、共享依赖治理、运行时加载和故障降级机制。

## 输入参数

| 参数名 | 类型 | 必填 | 说明 |
| -------- | ------ | ------ | ------ |
| HOST_APP | String | 是 | Host 应用信息 |
| REMOTE_APPS | String | 是 | Remote 应用列表 |
| BUILD_TOOL | String | 是 | 构建工具和版本 |
| SHARED_DEPENDENCIES | String | 是 | React、UI 库等共享依赖 |
| RUNTIME_REQUIREMENTS | String | 是 | 远程加载、缓存、降级要求 |
| DEPLOYMENT_MODEL | String | 否 | 部署域名、CDN、版本发布方式 |

## Prompt 正文

请基于以下信息，设计一套 Module Federation 接入方案，并输出配置示例与运行时治理建议。

**Host 应用：** {{HOST_APP}}
**Remote 应用：** {{REMOTE_APPS}}
**构建工具：** {{BUILD_TOOL}}
**共享依赖：** {{SHARED_DEPENDENCIES}}
**运行时要求：** {{RUNTIME_REQUIREMENTS}}
**部署模型：** {{DEPLOYMENT_MODEL}}

请完成以下任务：

1. 设计 Host 和 Remote 的职责划分与暴露模块规则。
2. 输出 Module Federation 配置示例和共享依赖策略。
3. 说明版本兼容、远程加载失败降级和缓存刷新方案。
4. 说明本地联调、测试和发布流程。
5. 给出风险和实施建议。

## 约束条件

1. 必须定义 Host 与 Remote 边界和暴露规则，不得让 Remote 任意泄露内部实现。
2. 必须说明共享依赖单例、版本策略和冲突处理，禁止产生多份核心运行时依赖。
3. 必须设计远程加载失败降级机制，禁止让 Remote 故障直接拖垮 Host。
4. 必须说明缓存失效和版本刷新策略，不得让旧版本静态资源长期污染线上流量。
5. 必须给出本地联调与发布流程，禁止只给生产配置不考虑开发体验。

## 输出要求

1. 输出 Host/Remote 架构说明。
2. 输出配置文件示例。
3. 输出依赖治理与降级方案。
4. 输出联调与发布流程。
5. 输出风险与注意事项。

6. 至少输出 1 个矩阵表、1 个流程图（可用 Mermaid 或等价文本流程）和 1 个风险清单（含风险、影响、缓解措施）。

## 输出格式

```markdown
# Module Federation 接入方案

## 1. 架构说明

## 2. 配置示例
```javascript
// module federation config
```

## 3. 共享依赖与版本治理

## 4. 降级、缓存与发布策略

## 5. 联调与风险建议

## 附录 A. 应用拆分与共享矩阵

| 应用/模块 | 边界职责 | 共享依赖 | 发布方式 | 隔离策略 |
| ------ | ------ | ------ | ------ | ------ |

## 附录 B. 流程图

（使用 Mermaid 或等价文本流程，至少包含：主应用装载 -> 子应用接入 -> 共享能力协同 -> 发布/回滚）

## 附录 C. 风险清单

| 风险 | 触发场景 | 影响 | 隔离/缓解措施 | 回退方式 |
| ------ | ------ | ------ | ------ | ------ |

## 自检清单

- [ ] 是否定义了 Host 与 Remote 边界
- [ ] 是否说明了共享依赖单例与版本策略
- [ ] 是否有运行时降级方案
- [ ] 是否定义了缓存与版本刷新机制
- [ ] 是否覆盖了联调与发布流程
