# AI Coding Prompt 模板库

[![skills.sh installs](https://skills.sh/b/yu-ying-stack/prompt-skills)](https://skills.sh/yu-ying-stack/prompt-skills) [![CI: validate-skills](https://github.com/yu-ying-stack/prompt-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/yu-ying-stack/prompt-skills/actions/workflows/validate-skills.yml)

> 研发团队 AI 编码提示词标准化工具包 —— 93 个专业 Prompt 模板，覆盖研发全流程 21 大场景。

## 特性

- **93 个标准化模板**：覆盖代码生成、审查、重构、测试、文档、Debug、架构设计、数据库、安全审计、性能优化、DevOps、可观测性、消息异步、需求评审、项目管理、版本控制、国际化、微前端、移动端、AI/ML、技术升级
- **LLM 无关**：适配 GPT / Claude / Gemini / 通义千问 / DeepSeek 等主流大模型
- **对话式交互**：无需记忆变量，AI 自动引导收集信息
- **团队规范统一**：所有成员使用相同的 Prompt 标准，保障输出质量
- **安全优先**：内置安全红线和禁止项，防止敏感信息泄露

## 快速安装

```bash
npx skills add yu-ying-stack/prompt-skills
```

## CI 状态

- [![CI: validate-skills](https://github.com/yu-ying-stack/prompt-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/yu-ying-stack/prompt-skills/actions/workflows/validate-skills.yml)  validate-skills — 在 PR 提交/更新 时运行，校验每个 `SKILL.md` 的 frontmatter 与示例文件是否存在。


安装后，在任意支持的 AI 代理中自然语言描述需求即可使用：

```text
"帮我生成一个 React 用户列表组件"
"review 一下这段 Python 代码"
"设计一个订单系统的数据库 Schema"
"这个接口性能太慢了，帮我排查"
```

## 支持的 AI 代理

- Claude Code
- Cursor
- GitHub Copilot
- Windsurf
- Qoder
- VS Code (GitHub Copilot)
- 以及 skills.sh 支持的 20+ 其他代理

## 模板分类

| 分类 | 模板数 | 典型场景 |
| ------ | ------ | --------- |
| 代码生成 | 8 | React组件、Python模块、API接口、Java服务、Go微服务、CLI工具 |
| 代码审查 | 6 | 前端/Python/Java/Go Review、SQL审查、PR审查 |
| 代码重构 | 6 | 遗留系统现代化、设计模式、单体拆微服务 |
| 测试生成 | 6 | 单元测试、集成测试、E2E、API契约、性能测试 |
| 文档生成 | 6 | API文档、架构文档、CHANGELOG、运维手册 |
| Debug排错 | 6 | 内存泄漏、并发问题、网络排查、生产事故 |
| 架构设计 | 6 | 系统设计、API设计、事件驱动、云原生 |
| 数据库设计 | 4 | Schema设计、查询优化、数据迁移、NoSQL建模 |
| 安全审计 | 4 | 代码安全、依赖审计、认证设计、隐私合规 |
| 性能优化 | 4 | 前端性能、后端性能、缓存策略 |
| DevOps与部署 | 5 | CI/CD、Docker、Kubernetes、IaC、灰度发布 |
| 可观测性 | 4 | 监控告警、Tracing、日志聚合、指标体系 |
| 消息与异步 | 4 | MQ设计、异步任务、事件驱动开发、死信治理 |
| 需求与评审 | 4 | PRD、设计评审、ADR、可行性评估 |
| 项目管理 | 3 | Story拆分、估算、风险评估 |
| 版本控制 | 2 | Git工作流、提交信息规范 |
| 国际化 | 2 | i18n方案设计、多语言测试与验证 |
| 微前端 | 3 | 微前端架构、模块联邦、跨应用状态管理 |
| 移动端 | 3 | React Native、移动性能、兼容性测试 |
| AI/ML | 5 | LLM应用、Prompt工程、模型训练、特征工程、模型评估 |
| 技术升级 | 2 | 主要依赖升级、大规模重构 |

## 使用方式

### 最简用法（推荐）

用自然语言描述你的需求，AI 会：

1. 自动匹配最合适的模板
2. 通过 1-2 个问题收集必要信息
3. 直接输出高质量结果

### 进阶用法

指定具体模板和参数：

```text
"用 API 接口生成模板，框架 FastAPI，数据库 PostgreSQL，认证 JWT"
```

## 项目结构

```text
skills/
└── ai-coding-prompts/
    ├── SKILL.md              # Skill 入口（元数据 + 使用指南）
    ├── references/           # 编码规范和使用指南
    │   ├── coding-standards.md
    │   └── prompt-usage-guide.md
    ├── templates/            # 93 个 Prompt 模板
    │   ├── code-generation/  (8个)
    │   ├── code-review/      (6个)
    │   ├── refactoring/      (6个)
    │   ├── testing/          (6个)
    │   ├── documentation/    (6个)
    │   ├── debugging/        (6个)
    │   ├── architecture/     (6个)
    │   ├── database/         (4个)
    │   ├── security/         (4个)
    │   ├── performance/      (4个)
    │   ├── devops/           (5个)
    │   ├── observability/    (4个)
    │   ├── async-messaging/  (4个)
    │   ├── requirements/     (4个)
    │   ├── project-management/ (3个)
    │   ├── version-control/  (2个)
    │   ├── internationalization/ (2个)
    │   ├── micro-frontend/   (3个)
    │   ├── mobile/           (3个)
    │   ├── ai-ml/            (5个)
    │   └── technology-upgrade/ (2个)
    └── examples/             # 使用示例与新模板导航
```

## 安全规范

使用本模板库时，请遵守以下安全红线：

- 禁止在 Prompt 中粘贴生产环境密钥/Token/密码
- 禁止要求 AI 生成绕过安全机制的代码
- AI 生成的代码必须经过人工审查后才能合入
- 禁止暴露用户隐私数据（PII）

详见 `references/prompt-usage-guide.md`。

## 贡献

欢迎提交 PR 贡献新模板或改进现有模板：

1. Fork 本仓库
2. 在对应分类目录下创建新模板（遵循 `references/coding-standards.md` 规范）
3. 提交 PR，描述模板用途和适用场景

## 许可证

MIT License
