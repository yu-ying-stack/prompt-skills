# OAuth2 实现检查与建议模板
---
元信息:
	模板名称: oauth2-implementation
	模板类型: security
	适用场景: 设计或审查 OAuth2 授权服务实现
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 设计或审查 OAuth2 授权服务实现

## 输入参数
- `grant_types`: 支持的授权类型
- `client_types`: 客户端类别

## Prompt 正文
给出安全实现要点、常见陷阱与合规建议（token 缩短、刷新策略、客户端认证）。
