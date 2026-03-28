---
created: '2026-02-18 13:25:04'
date: 2026-02-18
publish:
- Garden
tags:
- git
- architecture
- study
- antigravity
title: Git与Ag-OS架构实战复盘手册
ts: 1771392304
updated: '2026-02-19 23:17:02'
---

# 🛡️ Git 与 Antigravity-OS 双轨架构实战复盘

## 1. 核心架构设计：为何需要“双轨制”？

在构建 Antigravity-OS 时，我们面临一个核心矛盾：
*   **私密性 (Privacy)**：我的日记 (`000_Daily_Note`)、思考 (`Library_Study-Think`) 是绝对私人的，不能公开。
*   **公开性 (Publicity)**：我想把一部分精选内容 (`800_Digital_Garden`) 公开发布成网站，分享给世界。

为了解决这个矛盾，我们采用了 **“嵌套仓库 (Nested Repository)”** 的物理隔离方案。

### 📊 架构图解

```plaintext
【Antigravity-OS (私有大库)】
├── .git/ (私有历史记录)
├── Library_Study-Think/
│   ├── 000_Daily_Note/  🔒 (安全)
│   ├── ...
│   └── 800_Digital_Garden (Output)/ 🌍
│       ├── .git/ (公开历史记录 - 独立存在！)
│       ├── src/
│       ├── package.json
│       └── ...
└── Lab_Action/
```

**为什么这么做？**
1.  **物理隔离**：外层是大仓库，内层是小仓库。外层的 `.gitignore` 通常会忽略内层文件夹（或者由你手动管理）。
2.  **权限分离**：
    *   **外层** (`Antigravity-OS`) -> 推送到 GitHub **私有** 仓库。
    *   **内层** (`Digital-Garden`) -> 推送到 GitHub **公开** 仓库。
3.  **互不干扰**：你在内层 (`800_...`) 做的任何 `git commit`，只会记录在内层的 `.git` 里，不会污染外层。

---

## 2. 实战操作复盘：一步步拆解

今天下午，我们完整地执行了**内层公开库**的初始化与发布流程。以下是每一步的深度解析。

### Phase 1: 基地建设 (Init)

**操作命令**：
```bash
cd "Library_Study-Think/800_Digital_Garden (Output)"
git init
```

**发生了什么？**
Git 在当前目录下创建了一个隐藏的 `.git` 文件夹。
*   **此前**：这个文件夹只是电脑里的普通文件。
*   **此后**：它变成了一个受 Git 监控的“时空胶囊”，可以记录文件的所有变迁。

**为什么要改名 main？**
```bash
git branch -M main
```
*   **原因**：Git 默认分支名曾是 `master`，但为了响应我在github上看到它把master改成main，说是响应这个运动。解释啊下，现在全球标准已改为 `main`。GitHub 新建的仓库也默认叫 `main`，如果本地叫 `master`，推送时会产生不再需要的歧义。

### Phase 2: 防御工事 (.gitignore)

**操作与检查**：
我们确认了目录中存在 `.gitignore` 文件，且包含 `node_modules/`。

**原因**：
*   **体积爆炸**：`node_modules` 包含成千上万个小文件，体积巨大。
*   **无意义**：这些代码是 npm 从网上下载别人的库，不是你写的。只要有 `package.json`，任何人都能重新安装(`npm install`)出来，所以没必要存入你的 Git。
*   **Git 崩溃**：如果不忽略它，`git status` 会卡死。

### Phase 3: 暂存与提交 (Add & Commit)

**操作命令**：
```bash
git add .
git commit -m "feat: first launch of digital garden"
```

**原理解析**：
这是 Git 的核心三部曲：
1.  **工作区 (Workspace)**：你写代码的地方。
2.  **暂存区 (Staging Area)** (`git add`)：你不管是把文件“挑选”出来，放在一个“待发货”的箱子里。
3.  **版本库 (Repository)** (`git commit`)：你给箱子封口，贴上单号（Commit ID），永久保存。

**为什么分两步？**
有时候你改了10个文件，但只想提交其中3个（比如另外7个还没写完）。`git add` 给了你选择的权利。

### Phase 4: 连接云端 (Remote Add)

**操作命令**：
```bash
git remote add origin https://github.com/wygg/digital-garden.git
```

**解析**：
*   **Remote**：远程仓库的别名。
*   **Origin**：这是 Git 的惯例，代表“源头”或“默认远程仓库”。
*   这就好比在你的本地通讯录里，把那个长长的 URL 存为了一个叫 "origin" 的联系人。

### Phase 5: 点火发射 (Push)

**操作命令**：
```bash
git push -u origin main
```

**解析**：
*   **Push**：把本地的“提交记录”上传到云端。
*   **-u (upstream)**：这是一个“绑定”动作。
    *   **结果**：它告诉 Git，“以后我只要输入 `git push`（不带参数），你就默认推送到 `origin` 的 `main` 分支”。省去了以后打字的麻烦。

---

## 3. 面向未来 (Next Steps)

你的架构已经就绪。接下来的日常流程是：

1.  **写文章**：在 Obsidian 里写日记，打上 `#public` 标签。
2.  **同步**：运行 `python scripts/sync_garden.py`。
3.  **发布**：
    ```bash
    cd "Library_Study-Think/800_Digital_Garden (Output)"
    git add .
    git commit -m "feat: new post"
    git push
    ```
4.  **自动部署**：Vercel 监测到 GitHub 有变动，自动构建新网站。

🎉 **恭喜！你已经不仅是一个写作者，更是一个掌控自己数据流的工程师。**