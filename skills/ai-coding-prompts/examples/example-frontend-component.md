# 示例：使用前端组件生成模板

## 场景描述
为电商项目生成一个商品卡片组件。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| TECH_STACK | React 18 + TypeScript + TailwindCSS |
| COMPONENT_NAME | ProductCard |
| REQUIREMENT | 展示商品图片、名称、价格、折扣标签、加入购物车按钮；支持骨架屏加载态；响应式布局 |
| DESIGN_SPEC | 卡片圆角 8px，阴影 hover 时加深，图片 16:9 比例，价格红色高亮 |
| STATE_MANAGEMENT | 使用 Zustand 管理购物车状态 |

## 生成的完整 Prompt

你是一位拥有 8 年经验的高级前端工程师，精通 React 生态系统和现代前端最佳实践。

请为我生成一个 React 组件，要求如下：

**技术栈**：React 18 + TypeScript + TailwindCSS
**组件名称**：ProductCard
**功能需求**：展示商品图片、名称、价格、折扣标签、加入购物车按钮；支持骨架屏加载态；响应式布局
**设计规范**：卡片圆角 8px，阴影 hover 时加深，图片 16:9 比例，价格红色高亮
**状态管理**：使用 Zustand 管理购物车状态

**约束条件**：
1. 使用 TypeScript 严格模式，所有 Props 需有完整类型定义
2. 组件必须支持 ARIA 无障碍属性
3. 图片使用懒加载，并提供 fallback
4. 样式使用 TailwindCSS utility class，不使用内联样式
5. 包含完整的错误边界处理

**输出要求**：
1. 完整的组件文件（含类型定义）
2. Props 接口定义
3. 使用示例
4. 单元测试文件骨架

## 使用建议
- 生成后检查 TypeScript 类型是否完整
- 确认无障碍属性是否符合 WCAG 2.1 AA 标准
- 在移动端验证响应式布局效果
