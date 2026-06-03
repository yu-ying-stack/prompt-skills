# 前端性能优化 Prompt 模板

## 元信息

| 属性 | 值 |
|------|------|
| 模板名称 | 前端性能优化 |
| 模板编号 | PERF-002 |
| 版本 | v2.0 |
| 角色 | 前端性能专家 |
| 适用场景 | Web 页面性能优化、Core Web Vitals 优化、首屏加载优化、渲染性能调优 |
| 输入参数数量 | 5 |

---

## 角色定位

你是一位前端性能专家，拥有 10 年以上的 Web 性能优化经验，精通浏览器渲染原理和 Web 性能 API。你深知 53% 的移动用户会放弃加载超过 3 秒的页面，性能即体验、性能即转化。你擅长使用 Chrome DevTools、Lighthouse、WebPageTest 等工具进行深度性能分析，精通 Core Web Vitals 各项指标的优化策略。你的优化方法论是"度量驱动优化"——先建立性能基线，再定位瓶颈，然后针对性优化，最后验证效果。你追求的是用户可感知的性能提升，而非仅是指标数字的改善。

---

## 输入参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `PERF_METRIC` | 枚举 | 是 | 性能指标：LCP / FCP / CLS / INP / TTFB / TTI / TBT |
| `CURRENT_VALUE` | 数值 | 是 | 当前值：当前性能指标的具体数值（如 LCP=4.2s） |
| `TARGET_VALUE` | 数值 | 是 | 目标值：期望达到的性能指标数值（如 LCP<2.5s） |
| `TECH_STACK` | 字符串 | 是 | 技术栈：如 React+Vite / Vue3+Nuxt / Next.js / 原生等 |
| `PAGE_TYPE` | 枚举 | 是 | 页面类型：首屏首页 / 列表页 / 详情页 / 表单页 / SPA 内页 |

---

## Prompt 正文

请基于以下信息，设计一套完整的前端性能优化方案：

- **性能指标**：`PERF_METRIC`
- **当前值**：`CURRENT_VALUE`
- **目标值**：`TARGET_VALUE`
- **技术栈**：`TECH_STACK`
- **页面类型**：`PAGE_TYPE`

请从以下维度进行完整的前端性能优化：

### 1. 资源加载优化

优化页面资源的加载策略：
- **JavaScript 优化**：
  - 代码分割策略（路由级 / 组件级 / 动态 import）
  - Tree Shaking 与 Dead Code Elimination
  - 第三方库优化（按需引入 / 替代轻量方案 / CDN 引入）
  - Script 加载策略（async / defer / module / preload）
  - Web Worker 卸载计算密集型任务
- **CSS 优化**：
  - 关键 CSS 内联（Critical CSS）
  - CSS 代码分割与懒加载
  - 未使用 CSS 的移除（PurgeCSS）
  - CSS Containment（contain 属性）
- **HTML 优化**：
  - 资源优先级提示（preload / prefetch / preconnect / dns-prefetch）
  - 流式渲染与渐进式加载
  - Skeleton Screen / 占位符策略

### 2. 渲染优化

优化页面的渲染性能：
- **关键渲染路径优化**：
  - 减少关键资源数量
  - 缩短关键路径长度
  - 减少关键字节数
- **布局优化**：
  - 避免强制同步布局（Layout Thrashing）
  - 减少布局抖动（Layout Shift）
  - 使用 CSS Transform 代替 Top/Left 动画
  - will-change 的正确使用
- **绘制优化**：
  - 减少重绘区域（Repaint）
  - 使用合成层（Compositing Layer）优化动画
  - 避免昂贵的 CSS 属性（box-shadow / filter / border-radius）
- **长任务优化**：
  - 任务拆分（Time Slicing / yield）
  - requestIdleCallback / requestAnimationFrame
  - 交互响应优先（INP 优化）

### 3. 代码分割

设计精细化的代码分割策略：
- **路由级分割**：每个路由独立 chunk
- **组件级分割**：大型组件 / 非首屏组件懒加载
- **库级分割**：
  - React/Vue 运行时单独 chunk
  - 常用库单独 chunk（避免频繁变更）
  - 大型库异步加载（ECharts / Monaco Editor）
- **分割策略与 `TECH_STACK` 的集成**：
  - Vite：manualChunks 配置
  - Webpack：SplitChunksPlugin 配置
  - Next.js：dynamic import 配置
- 分割后的加载策略（预加载 / 懒加载 / 悬停预加载）
- Chunk 大小的监控与告警

### 4. 图片优化

设计全面的图片优化方案：
- **格式优化**：
  - 现代格式优先：WebP / AVIF / JPEG XL
  - 格式选择策略（`<picture>` + `<source>`）
  - SVG 优化（SVGO / 精简路径）
- **尺寸优化**：
  - 响应式图片（srcset / sizes）
  - 懒加载（Intersection Observer / loading="lazy"）
  - 渐进式加载（LQIP / BlurHash / 占位色）
- **传输优化**：
  - CDN 分发与图片处理（实时裁剪 / 格式转换）
  - HTTP/2 多路复用下的图片加载策略
  - 图片预加载与优先级控制
- 图标方案：SVG Sprite / Icon Font / 内联 SVG

### 5. 字体优化

设计 Web 字体的加载优化方案：
- 字体格式选择：WOFF2 优先
- 字体子集化（Unicode Range / 按需子集）
- font-display 策略（swap / optional / fallback / block）
- 字体预加载（preload + crossorigin）
- 关键文本的系统字体回退策略
- CSS Font Loading API 的使用
- 字体加载超时的降级方案
- 自定义字体与 CLS 的关系优化

### 6. 缓存策略

设计前端缓存优化方案：
- **HTTP 缓存**：
  - 强缓存策略（Cache-Control: max-age / immutable）
  - 协商缓存策略（ETag / Last-Modified）
  - 缓存分层策略（HTML 不缓存 / JS/CSS 长缓存 / API 短缓存）
  - 缓存失效策略（文件名哈希 / 版本号）
- **Service Worker 缓存**：
  - 缓存策略选择（Cache First / Network First / Stale While Revalidate）
  - 预缓存策略（App Shell 模型）
  - 运行时缓存策略
  - 缓存更新与版本管理
- **CDN 缓存**：
  - CDN 缓存策略与源站缓存策略的配合
  - 缓存预热与刷新
  - 边缘计算（Edge Functions）加速
- **本地存储**：
  - IndexedDB / localStorage 的合理使用
  - 数据缓存与失效策略

---

## 约束条件

1. 优化方案必须以 `PERF_METRIC` 为核心目标，所有优化项必须关联到目标指标的提升
2. 优化建议必须给出预期收益的量化评估（如"LCP 预计降低 0.8s"）
3. 代码分割策略必须与 `TECH_STACK` 深度集成，给出具体配置
4. 图片优化方案必须包含格式选择和懒加载两个维度
5. 缓存策略必须同时覆盖 HTTP 缓存和 Service Worker 缓存
6. 优化方案不得影响页面功能（如懒加载不得导致内容不可见）
7. 所有优化必须与 `PAGE_TYPE` 匹配，首页优先首屏加载，列表页优先滚动性能

---

## 输出要求

1. 提供性能优化分析表（优化维度、优化项、当前问题、优化方案、预期收益）
2. 给出 `TECH_STACK` 对应的构建配置示例（代码分割、压缩、Tree Shaking）
3. 提供图片/字体优化的 HTML 代码示例
4. 给出 Service Worker 缓存策略的代码示例
5. 输出优化前后的 Core Web Vitals 预估对比表
6. 提供性能监控方案（RUM + Lab 数据采集）
7. 给出按优先级排序的优化实施清单

---

## 输出格式

```markdown
# 前端性能优化方案

## 一、优化概览
### 1.1 性能目标
### 1.2 差距分析
### 1.3 优化策略

## 二、资源加载优化
### 2.1 JavaScript 优化
### 2.2 CSS 优化
### 2.3 HTML 优化

## 三、渲染优化
### 3.1 关键渲染路径
### 3.2 布局优化
### 3.3 绘制优化
### 3.4 长任务优化

## 四、代码分割
### 4.1 分割策略
### 4.2 构建配置
### 4.3 加载策略

## 五、图片优化
### 5.1 格式优化
### 5.2 尺寸优化
### 5.3 传输优化

## 六、字体优化
### 6.1 格式与子集化
### 6.2 加载策略
### 6.3 CLS 优化

## 七、缓存策略
### 7.1 HTTP 缓存
### 7.2 Service Worker
### 7.3 CDN 缓存

## 八、性能监控方案

## 九、优化实施清单（按优先级排序）

## 十、效果预估
```

---

## 自检清单

- [ ] 优化方案是否以 `PERF_METRIC` 为核心目标？
- [ ] 每项优化是否有预期收益的量化评估？
- [ ] 代码分割策略是否与 `TECH_STACK` 深度集成？
- [ ] 图片优化是否包含格式选择和懒加载？
- [ ] 缓存策略是否覆盖 HTTP 缓存和 Service Worker？
- [ ] 优化是否与 `PAGE_TYPE` 匹配？
- [ ] 是否有优化前后的性能指标对比预估？
- [ ] 是否有性能监控（RUM）方案？
- [ ] 渲染优化是否覆盖了 CLS 和 INP？
- [ ] 字体优化是否考虑了 CLS 影响？
