# CI 并行化优化模板
## 元信息
- 场景: 将单序列 CI 流水线改为并行以降低总时长
## 输入参数
- `jobs`: 当前 CI 作业与耗时
- `dependencies`: 作业间依赖关系
## Prompt 正文
输出并行化方案、缓存策略与可能的 flaky 风险点，并给出步骤与示例 GitHub Actions 配置片段。
