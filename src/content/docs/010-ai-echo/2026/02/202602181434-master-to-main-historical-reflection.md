---
created: '2026-02-18 14:34:15'
date: 2026-02-18
publish:
- Garden
tags:
- Life/日记
- Culture/Tech
- Git/History
title: Master 到 Main：代码世界的文化重构与反思
ts: 1771396455
updated: '2026-02-19 23:17:02'
---

# 📅 2026-02-18 Master 到 Main：代码世界的文化重构与反思

## 🎯 今日专注 (Focus)
- [x] 了解 Git 默认分支从 `master` 变更为 `main` 的历史背景 (Gemini Re-study)。
- [x] 反思技术术语背后的文化隐喻与社会责任。

## 🧠 学 (Study)
> 记录今天的输入：Gemini 关于 BLM 运动与 Git 重命名的对话整理

今天在使用 Git 初始化仓库时，遇到了一行提示 `hint: Using 'master' as the name for the initial branch...`，这引发了我对技术与时代关系的深究。

经过 Gemini 的梳理，我了解到：
1.  **导火索**：2020 年的 **BLM (Black Lives Matter)** 运动。
2.  **核心争议**：虽然 `master` 在 Git 里本意多指 "Master Copy"，但在计算机领域长期存在的 **Master/Slave**（主/从）架构术语，不可避免地让人联想到奴隶制的历史创伤。
3.  **行业响应**：GitHub CEO Nat Friedman 在 2020 年 6 月响应社区呼声，并在 10 月正式将新建仓库默认分支改为 `main`。
4.  **去政治化努力**：技术界随之掀起了一场术语清洗运动：
    *   `Whitelist/Blacklist` -> `Allowlist/Denylist`
    *   `Master/Slave` -> `Main/Replica`

这已经成为了不可逆转的 **"Political Correctness Industry Standard"** (政治正确后的行业标准)。

## 💡 思 (Think)
> 记录今天的思考：

**技术从来不是中立的。**
代码虽然是 0 和 1，但写代码的人生活在具体的社会语境中。一个变量名、一个分支名，都潜移默化地折射着那个时代的价值观。

从 `master` 到 `main` 的迁移，表面上增加了老项目的维护成本（各种 CI/CD 脚本报错），但从长远看，它体现了技术社区的一种 **"Inclusive Engineering" (包容性工程)** 理念。

作为个体开发者，我也许无法改变世界，但顺应这种变化（比如今天主动把 `800_Digital_Garden` 初始化为 `main`），不仅是为了避免技术债，也是一种对多元文化的尊重。

## ⚡ 行 (Action)
> 记录今天的产出：

1.  在 Antigravity-OS 的所有新仓库中，**强制使用 `main` 作为默认分支**。
2.  记录下这段技术史，提醒自己：写代码时，也要保持对他人的同理心。

---
#public