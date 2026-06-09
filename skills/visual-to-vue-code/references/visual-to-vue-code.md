# 视觉转 Vue Skill 参考说明

该文档摘取自 `docs/visual-to-vue-code-skill.md`，包含能力边界、五阶段流水线、Visual IR schema、组件映射表与自检清单。实现时请参照 `skills/ai-coding-prompts/references/coding-standards.md` 的变量与占位符约定。

关键约束：

- 输出必须包含 Visual IR（JSON）与自检报告
- 模板正文中占位符使用 `{{VAR_NAME}}`
- YAML frontmatter 的 `triggers` 列表必须缩进正确，避免解析错误
