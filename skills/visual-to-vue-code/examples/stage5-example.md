# Stage5 示例 - 自检报告示例

输入：生成的项目清单与源码

用户指令："输出自检报告，列出未解决的 TODO 和需要人工确认的项。"

期望输出（摘要）：

```markdown
## 自检报告
- [x] 视觉完整性：已映射 header/sidebar/table/button
- [x] 组件正确性：表格使用 `el-table`，按钮使用 `el-button`
- [ ] 类型安全：某些组件的 props 需补充 TS 类型
- [ ] 运行性：需执行 `npm install` 验证依赖

### TODO
- 补充表格列类型与后端字段映射
- 确认手绘草图中不清晰的文本
```
