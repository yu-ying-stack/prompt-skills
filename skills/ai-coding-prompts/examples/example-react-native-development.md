# 示例：使用 React Native 开发模板

## 场景描述

开发一个支持拍照上传票据、OCR 识别和报销提交的 React Native 页面。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| FEATURE_REQUIREMENT | 报销单创建页面，支持拍照上传票据、OCR 识别金额、编辑并提交 |
| APP_STACK | React Native 0.76、React Navigation、Zustand、原生相机模块 |
| TARGET_PLATFORMS | iOS + Android |
| DESIGN_CONSTRAINTS | 需符合企业设计系统，支持深色模式和离线草稿 |
| DEVICE_CAPABILITIES | 相机、相册、文件选择、离线存储、推送通知 |
| QUALITY_REQUIREMENTS | 首屏 2 秒内可交互，关键动作埋点，需提供组件测试和 E2E 建议 |

## 可直接使用的 Prompt

请基于以下信息，设计一套 React Native 开发方案，并输出实现结构、代码建议和测试策略。

**功能需求：** {{FEATURE_REQUIREMENT}}
**应用栈：** {{APP_STACK}}
**目标平台：** {{TARGET_PLATFORMS}}
**设计约束：** {{DESIGN_CONSTRAINTS}}
**设备能力：** {{DEVICE_CAPABILITIES}}
**质量要求：** {{QUALITY_REQUIREMENTS}}

请重点说明权限处理、离线草稿和 OCR 失败降级策略。