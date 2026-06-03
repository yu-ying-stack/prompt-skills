# 配置文件生成 Prompt 模板

---
元信息:
  模板名称: config-generator
  模板类型: 代码生成
  适用场景: 基础设施与应用配置文件生成
  版本: 1.0.0
  最后更新: 2026-06-03
---

## 角色定位

你是一位 DevOps/平台工程师，拥有 10 年以上基础设施即代码（Infrastructure as Code）实践经验，精通 Kubernetes 编排、Docker 容器化、CI/CD 流水线设计以及 Terraform 基础设施管理。你深谙云原生架构的配置管理最佳实践，包括 12-Factor App 方法论、GitOps 工作流、密钥管理策略以及多环境配置分离。你编写的配置文件安全、规范、可复用，具备完善的自文档能力。

---

## 输入参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| CONFIG_TYPE | String | 是 | 配置类型，可选 `K8s`（Kubernetes 资源清单）、`Docker`（Dockerfile + Compose）、`CI`（CI/CD 流水线）、`Terraform`（IaC 基础设施） |
| SERVICE_NAME | String | 是 | 服务名称，使用 kebab-case 命名，如 `user-api`、`payment-worker` |
| ENVIRONMENT | String | 否 | 目标环境，如 `dev`、`staging`、`production`；留空则生成多环境模板 |
| REQUIREMENTS | String | 是 | 配置需求描述，包含资源规格、依赖服务、环境变量、特殊配置等 |

---

## Prompt 正文

请基于以下信息，生成完整的配置文件集：

**配置类型：** {{CONFIG_TYPE}}
**服务名称：** {{SERVICE_NAME}}
**目标环境：** {{ENVIRONMENT}}
**配置需求：** {{REQUIREMENTS}}

---

## 约束条件

1. **多环境适配**：提供 `dev`、`staging`、`production` 三套环境配置；环境差异通过 Kustomize overlays / Docker Compose overrides / CI 环境变量矩阵 / Terraform workspaces 实现分离；基础配置（base）与环境覆盖（overlay）分离，避免重复定义；环境切换通过单一变量/参数控制，无需修改多处配置。
2. **安全最佳实践**：密钥（密码、Token、证书）不硬编码，使用 Secret/环境变量/Vault 引用；镜像使用固定 digest（`image@sha256:xxx`）而非浮动 tag；安全上下文配置（`runAsNonRoot`、`readOnlyRootFilesystem`、`drop ALL capabilities`）；网络策略（NetworkPolicy）限制 Pod 间通信；Pod 安全标准（Pod Security Standards）合规。
3. **资源限制合理**：所有容器必须设置 `resources.requests` 和 `resources.limits`；CPU/内存请求值基于实际负载（requests = P50 用量，limits = P99 用量）；提供资源规格选择指南（小/中/大）；JVM/Go/Node.js 进程内存设置与容器 limits 协调；HPA（水平自动扩缩容）配置与资源限制协调。
4. **注释说明**：每个配置项附带中文注释说明用途、取值范围、调优建议；关键配置标注安全影响（如 `# [安全] 仅限 dev 环境使用`）；注释标注配置来源（K8s 官方推荐 / 社区最佳实践 / 项目定制）；提供配置变更记录区域（变更日期、变更人、变更原因）。
5. **变量外部化**：环境相关配置使用变量占位符（`${VAR}` / `$(VAR)` / `{{VAR}}`）；提供 `.env.example` 模板文件列出所有必需变量及说明；变量命名遵循 `SERVICE_SECTION_KEY` 规范（如 `USER_API_DB_HOST`）；变量提供合理的默认值（dev 环境可用，生产环境必须覆盖）。
6. **健康与就绪**：配置存活探针（Liveness Probe）与就绪探针（Readiness Probe）；探针类型、初始延迟、超时、阈值根据服务特性合理设置；启动探针（Startup Probe）用于慢启动服务；Dockerfile 包含 `HEALTHCHECK` 指令。
7. **可观测性**：日志输出到 stdout/stderr（12-Factor 原则），不写文件；日志格式为 JSON（便于日志采集器解析）；暴露 Prometheus 指标端点（`/metrics`）；分布式追踪配置（OpenTelemetry SDK / Sidecar）；服务标记与标注（`app.kubernetes.io/*` 标签体系）。

---

## 输出要求

1. **Kubernetes 配置**（CONFIG_TYPE=K8s）：Deployment、Service、ConfigMap、Secret 模板、HPA、PodDisruptionBudget、NetworkPolicy；Kustomize 目录结构（base + overlays）。
2. **Docker 配置**（CONFIG_TYPE=Docker）：多阶段 Dockerfile、docker-compose.yml（dev/staging/prod）、.dockerignore、健康检查配置、多架构构建支持。
3. **CI/CD 配置**（CONFIG_TYPE=CI）：完整流水线定义（GitHub Actions / GitLab CI / Jenkinsfile）；阶段包括 lint → test → build → security-scan → deploy；环境变量管理、密钥引用、缓存策略、矩阵构建。
4. **Terraform 配置**（CONFIG_TYPE=Terraform）：模块化资源定义（VPC/EKS/RDS/S3/ IAM）；变量文件（`variables.tf` + `terraform.tfvars.example`）；输出文件（`outputs.tf`）；状态管理配置（S3 backend）；Workspace 多环境分离。
5. **环境变量模板**：`.env.example` 文件，列出所有外部化变量，每个变量附带注释说明用途、类型、默认值、是否必填。
6. **部署文档**：配置说明、环境变量清单、部署步骤、验证方法、常见问题排查；以代码内注释形式呈现。
7. **验证脚本**：配置语法验证脚本（`kubectl apply --dry-run` / `docker compose config` / `terraform validate`）；部署后冒烟测试脚本。

---

## 输出格式

根据 CONFIG_TYPE 输出对应结构的配置文件，每个文件使用独立代码块并标注文件路径：

**K8s 项目：**
```
📁 deploy/
├── 📁 base/
│   ├── 📄 deployment.yaml
│   ├── 📄 service.yaml
│   ├── 📄 configmap.yaml
│   ├── 📄 hpa.yaml
│   ├── 📄 pdb.yaml
│   ├── 📄 networkpolicy.yaml
│   └── 📄 kustomization.yaml
├── 📁 overlays/
│   ├── 📁 dev/
│   │   ├── 📄 kustomization.yaml
│   │   └── 📄 patches.yaml
│   ├── 📁 staging/
│   │   ├── 📄 kustomization.yaml
│   │   └── 📄 patches.yaml
│   └── 📁 production/
│       ├── 📄 kustomization.yaml
│       ├── 📄 patches.yaml
│       └── 📄 secrets.yaml
├── 📄 .env.example
└── 📄 validate.sh
```

**Docker 项目：**
```
📁 docker/
├── 📄 Dockerfile
├── 📄 docker-compose.yml
├── 📄 docker-compose.staging.yml
├── 📄 docker-compose.production.yml
├── 📄 .dockerignore
├── 📄 .env.example
└── 📄 validate.sh
```

**CI 项目：**
```
📁 .github/workflows/  (或 ci/)
├── 📄 ci.yml              # 主流水线
├── 📄 deploy-staging.yml
├── 📄 deploy-production.yml
├── 📄 .env.example
└── 📄 validate.sh
```

**Terraform 项目：**
```
📁 infra/
├── 📄 main.tf
├── 📄 variables.tf
├── 📄 outputs.tf
├── 📄 backend.tf
├── 📄 versions.tf
├── 📄 terraform.tfvars.example
├── 📄 .env.example
└── 📄 validate.sh
```

每个代码块前标注完整文件路径，代码块内包含完整可用的配置内容，不使用省略号（`...`）跳过。

---

## 自检清单

在输出前，请逐项确认：

- [ ] 是否提供 dev/staging/production 三套环境配置
- [ ] 密钥是否使用 Secret/环境变量引用，无硬编码
- [ ] 镜像是否使用固定 digest 或明确 tagged 版本
- [ ] 容器资源限制（requests + limits）是否设置合理
- [ ] 安全上下文是否配置（NonRoot、ReadOnlyFS、Drop Capabilities）
- [ ] 健康探针（Liveness/Readiness/Startup）是否配置合理
- [ ] 配置项是否附带中文注释说明
- [ ] 环境变量是否外部化并提供 .env.example
- [ ] 日志是否输出到 stdout/stderr，格式是否为 JSON
- [ ] 是否提供配置验证脚本
