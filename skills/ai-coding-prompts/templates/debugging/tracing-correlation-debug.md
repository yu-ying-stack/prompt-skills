# 分布式追踪关联问题诊断模板
---
元信息:
	模板名称: tracing-correlation-debug
	模板类型: debugging
	适用场景: 诊断 trace id / span 丢失或链路断裂问题
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 诊断 trace id / span 丢失或链路断裂问题

## 输入参数
- `trace_sample`: 失败请求的 trace 样例
- `topology`: 服务调用拓扑

## Prompt 正文
分析可能的原因并给出排查步骤、日志增强建议与代码级修复点。
