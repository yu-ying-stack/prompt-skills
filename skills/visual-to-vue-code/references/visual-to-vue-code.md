# 视觉转 Vue Skill 参考说明

该文档摘取并浓缩自 `docs/visual-to-vue-code-skill.md`，包含可复用片段（Visual IR schema、组件映射片段、设计 Token 示例、Stage 示例引用）。实现时请参照 `skills/ai-coding-prompts/references/coding-standards.md` 的变量与占位符约定。

## 可复用片段

### Visual IR Schema（片段）

```json
{"meta":{"imageType":"ui-screenshot|hand-drawn-sketch","confidence":"high|medium|low","pageType":"dashboard|list-page|form-page"},"layout":{"structure":"sidebar-main|topnav-main|card-grid"}}
```

### 组件映射（片段）

```
主按钮 => el-button type="primary"
表格 => el-table (封装 DataTable.vue)
弹窗 => el-dialog
```

### 设计 Token（片段）

```css
:root{--vt-primary-color:#409EFF;--vt-space-md:16px}
```

## Stage 示例索引

- Stage1 示例（高置信）： `examples/stage1-high-confidence.md`
- Stage1 示例（低置信）： `examples/stage1-low-confidence.md`
- Stage2 示例： `examples/stage2-example.md`
- Stage3 示例： `examples/stage3-example.md`
- Stage4 示例： `examples/stage4-example.md` （并参见 templates/stage4-samples.md）
- Stage5 示例： `examples/stage5-example.md`

## Chain-of-Thought 模板（可复用）

在 Stage1 输出时，推荐包含简短 Chain-of-Thought，长度 ≤ 8 行，结构如下：

```
1. 识别布局类型并说明依据（例如：顶部横幅高度 + 菜单项 → topnav）
2. 为关键视觉元素指定候选组件（例如：大表格 → el-table, 操作按钮 → el-button）
3. 识别数据关系（例如：按钮触发表格刷新 → table-refresh）
4. 标注低置信度区域并建议人工确认字段
```

## 更详尽的示例索引

- Stage1 多页示例： `examples/stage1-multi-page.md`
- Stage1 图表重示例： `examples/stage1-chart-heavy.md`
- Stage2 复杂交互： `examples/stage2-complex-interactions.md`
- Stage3 响应式网格： `examples/stage3-responsive-grid.md`
- Stage4 完整项目样例： `examples/stage4-full-sample.md`


## 约束与注意事项

- 输出必须包含 Visual IR（JSON）与自检报告
- 模板正文中占位符使用 `{{VAR_NAME}}`
- YAML frontmatter 的 `triggers` 列表必须缩进正确
