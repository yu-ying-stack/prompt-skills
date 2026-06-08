# 示例：使用消息队列设计模板

## 场景描述

为订单创建后的库存扣减、优惠券核销和通知发送设计 Kafka 消息系统。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| BUSINESS_SCENARIO | 订单创建后需要异步扣减库存、核销优惠券、发送站内通知和短信 |
| MESSAGE_PLATFORM | Kafka |
| THROUGHPUT_REQUIREMENTS | 日常 5k TPS，活动峰值 30k TPS，端到端延迟小于 2 秒 |
| DELIVERY_GUARANTEE | 至少一次投递，消费端幂等 |
| CONSUMER_PATTERNS | 竞争消费、失败重试、DLQ、按订单号分区保证局部有序 |
| FAILURE_SCENARIOS | 库存服务超时、优惠券服务重复消费、短信服务失败重试 |

## 可直接使用的 Prompt

请基于以下信息，设计一套消息队列方案，并说明主题、消费和容错治理策略。

**业务场景：** {{BUSINESS_SCENARIO}}
**消息平台：** {{MESSAGE_PLATFORM}}
**吞吐要求：** {{THROUGHPUT_REQUIREMENTS}}
**投递保障：** {{DELIVERY_GUARANTEE}}
**消费模式：** {{CONSUMER_PATTERNS}}
**失败场景：** {{FAILURE_SCENARIOS}}

请重点说明主题设计、幂等、重试和死信处理。