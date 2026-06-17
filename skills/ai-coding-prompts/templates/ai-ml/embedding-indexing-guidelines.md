# Embedding 索引与检索指南模板
---
元信息:
	模板名称: embedding-indexing-guidelines
	模板类型: ai-ml
	适用场景: 为向量检索系统设计 embedding 生成与索引策略
	版本: 1.0.0
	最后更新: 2026-06-17
---

## 元信息
- 场景: 为向量检索系统设计 embedding 生成与索引策略

## 输入参数
- `corpus`: 文档类型与数量级

## Prompt 正文
给出 embedding 维度选择、归一化、向量索引类型（HNSW/IVF）与更新策略建议。

## 输出要求
- 建议的 embedding 维度与选择理由
- 向量索引类型比较（HNSW/IVF 等），含参数建议
- 索引更新与再索引策略
- 示例命令/代码片段（示例使用 Faiss/Weaviate/Elasticsearch）

## 自检清单
- 是否给出了明确的维度选择原则
- 是否包含向量归一化与距离度量建议
- 是否包含示例索引构建或查询代码片段
- 是否说明了索引维护成本与再索引策略
