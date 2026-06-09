# Stage4 示例 - 完整最小可运行项目清单与说明

目标：提供一个更完整的最小项目示例，供 Stage4 直接输出并用于 smoke test。

包含文件（示例）：

- `package.json`（见 templates/stage4-samples.md）
- `vite.config.ts`（简化）
- `tsconfig.json`（简化）
- `src/main.ts`, `src/App.vue`, `src/components/AppHeader.vue`, `src/components/DataTable.vue`

运行步骤建议：

```bash
npm install
npm run dev
```

注意：在生成时需确保 `src/components` 中使用的路径别名 (`@/`) 在 `tsconfig.json` 与 `vite.config.ts` 中配置一致。
