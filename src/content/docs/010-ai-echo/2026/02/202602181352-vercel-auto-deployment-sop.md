---
created: '2026-02-18 13:52:28'
date: 2026-02-18
publish:
- Garden
tags:
- vercel
- deployment
- ci-cd
- study
title: Vercel自动化发布技术复盘与SOP
ts: 1771393948
updated: '2026-02-19 23:17:02'
---

# 🚀 从 GitHub 到 Vercel：自动化发布全流程复盘

## 1. 原理揭秘：网站是怎么变出来的？

在以前，要把网站挂到网上，你得：
1.  买服务器 (云主机)
2.  装 Nginx/Apache
3.  配置 Linux 环境
4.  手动把文件传上去 (FTP/SCP)

而在 Vercel 时代，这一套变成了 **CI/CD (持续集成/持续部署)** 自动化流水线。

**核心机制：Webhook (钩子)**

当你在本地执行 `git push` 时：
1.  **触发**：GitHub 接收到代码，立刻向 Vercel 发送一个 HTTP 请求（Webhook）。
2.  **响应**：Vercel 收到消息：“嘿，wygg 更新代码了！”
3.  **拉取**：Vercel 的服务器立刻从 GitHub 把你的代码拉下来。
4.  **构建**：Vercel 在它的云端容器里运行 `npm install` 和 `npm run build`。
5.  **分发**：构建好的静态文件 (HTML/CSS/JS) 被推送到全球 CDN 节点。

---

## 2. 详细步骤复盘 (SOP)

### Phase 1: 建立连接 (Link)

**操作动作**：
在 Vercel控制台点击 `Import Project` -> 选择 `digital-garden` 仓库。

**技术细节**：
*   **授权 (OAuth)**：Vercel 获得了读取你 GitHub 这个特定仓库的权限。
*   **配置识别**：Vercel 会自动扫描 `package.json`。
    *   发现 `astro` 依赖 -> 判定为 Astro 框架。
    *   自动设置 Build Command: `astro build`。
    *   自动设置 Output Directory: `dist` (这是 Astro 默认的输出目录)。

### Phase 2: 构建流水线 (Build Pipeline)

当你点击 Deploy 后，Vercel 后台发生了什么？（你可以在 Deployment -> Logs 里看到这些）

1.  **Clone**：`git clone https://github.com/wygg/digital-garden.git`
2.  **Dependencies**：`npm install`
    *   下载 `astro`, `react`, `tailwindcss` 等数千个包。
    *   这就是为什么我们**不需要**把 `node_modules` 上传到 GitHub，因为 Vercel 会根据 `package.json` 里的清单重新下载一份。
3.  **Build**：`npm run build` (即 `astro build`)
    *   **Astro 的工作**：它会把你的 `.astro` 和 `.md` 文件编译成纯 HTML。
    *   **静态生成 (SSG)**：它会执行 `getStaticPaths`，为每一篇 Markdown 文章生成一个独立的 HTML 页面。
4.  **Upload**：
    *   生成的 `dist/` 文件夹（里面全是 HTML/CSS/JS/图片）被上传到 Vercel 的存储桶。

### Phase 3: 全球分发 (Edge Network)

这是最神奇的一步。
Vercel 不只是把文件放那儿，而是推送到全球数百个 **Edge (边缘) 节点**。

*   **结果**：
    *   美国用户访问 -> 路由到美国节点
    *   中国用户访问 -> 路由到香港/新加坡/日本节点
    *   速度极快，无需你自己配置 CDN。

---

## 3. 常见问题排查 (Troubleshooting)

### Q: 为什么 Vercel 报错 "Command not found: astro"?
*   **原因**：因为 `package.json` 里没有把 `astro` 列为 `dependencies`，或者你把 `node_modules` 上传了导致冲突。
*   **解法**：确保本地能跑通 `npm run build`，且 `.gitignore` 包含了 `node_modules`。

### Q: 为什么文章更新了，网站没变？
*   **原因**：可能是 Vercel 构建失败（比如某篇 Markdown 格式错误导致编译挂了）。
*   **解法**：去 Vercel Dashboard 看最新的 Deployment Logs，如果是红色的 Error，即使 GitHub 显示 push 成功，网站也不会更新。

### Q: 如何自定义域名？
*   **操作**：Vercel -> Settings -> Domains。
*   你可以买一个 `wygg.com`，然后在域名商那里添加 CNAME 记录指向 `cname.vercel-dns.com`。

---

## 4. 你的“发布按钮”

现在，你的发布流程简化为：

**写完文章 -> 运行 Sync 脚本 -> Git Push**

剩下的所有（构建、分发、刷新缓存），Vercel 全帮你做了。这就是现代工程化的力量。

---

## 5. Antigravity Iron Workflow (执行摘要)

这是经过我们反复推演确认的 **“知行合一”标准作业程序**：

1.  **Private Source (私密创作)** 📝
    *   **位置**：Obsidian (`Library_Study-Think`)
    *   **动作**：自由书写，只给想公开的文章打上 `#public` 标签。

2.  **Sync Filter (脚本过滤)** ⚙️
    *   **命令**：`python scripts/sync_garden.py`
    *   **动作**：物理拷贝 `#public` 文件到 `800_Digital_Garden (Output)`。这是私有与公开的物理分界线。

3.  **Local Preview (本地预演)** 👀
    *   **位置**：`localhost:4323`
    *   **动作**：在本地浏览器检查文章排版。不满意就回 Obsidian 改，改完再 Sync。

4.  **Audit & Push (审核与发布)** 🚀
    *   **命令**：`git add . && git commit && git push` (在 `800_...` 目录下)
    *   **意义**：这是唯一的 **Gatekeeper**。你按下回车的那一刻，就是向世界广播。

5.  **Cloud Build (云端构建)** ☁️
    *   **位置**：Vercel
    *   **动作**：自动拉取、构建、分发到全球。无需人工干预。