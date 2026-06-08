# 示例：使用国际化与本地化设计模板

## 场景描述

为一个面向东南亚市场的 SaaS 后台设计中英泰三语国际化方案。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| PRODUCT_SCOPE | React 管理后台、营销邮件模板和部分移动端页面 |
| TARGET_LOCALES | zh-CN、en-US、th-TH |
| I18N_STACK | React Intl、FormatJS、Node.js 邮件模板服务 |
| CONTENT_TYPES | UI 文案、表单校验文案、邮件模板、帮助中心标题 |
| LOCALIZATION_RULES | 货币支持 CNY/USD/THB，日期按地区格式化，保留时区设置 |
| TRANSLATION_WORKFLOW | 使用 Crowdin 管理翻译，产品初审，运营终审，每周同步一次 |

## 可直接使用的 Prompt

请基于以下信息，设计一套国际化与本地化方案，并输出工程与运营协作规则。

**产品范围：** {{PRODUCT_SCOPE}}
**目标语言地区：** {{TARGET_LOCALES}}
**技术栈：** {{I18N_STACK}}
**内容类型：** {{CONTENT_TYPES}}
**本地化规则：** {{LOCALIZATION_RULES}}
**翻译流程：** {{TRANSLATION_WORKFLOW}}

请重点说明文案资源管理、回退机制和翻译发布流程。