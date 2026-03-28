---
created: '2026-02-18 21:14:54'
date: 2026-02-18
publish:
- Garden
tags:
- Tutorial
- Cloudflare
- R2
- Tools
- Public
title: 零成本打造全球加速图床：Cloudflare R2 实战白嫖指南
ts: 1771420494
updated: '2026-02-19 23:17:02'
---

# 🚀 零成本打造全球加速图床：Cloudflare R2 实战白嫖指南

> **背景**：在构建 Antigravity OS（数字花园）的过程中，我们面临一个痛点：图片存 Git 仓库太重，存第三方图床怕跑路。Cloudflare R2 给了我们“真香”的中间方案：**10GB 永久免费空间、0 流量费（无 Egress 费用）、全球 CDN 加速。**

本教程记录了作者从“开门”到“配钥匙”的全过程，适合想彻底解决图片存储焦虑的同学。

---

## 🏗️ 第一阶段：开启大门 (注册与核验)

R2 是 Cloudflare 旗下的对象存储服务。虽然它是免费的，但为了防止恶意滥用，它有一个“进门门槛”。

1.  **准备工作**：一个 Cloudflare 账号，一张外币信用卡（Visa/MasterCard）或 PayPal 账号。
2.  **绑定支付方式**：
    *   在 R2 页面填入支付信息。
    *   **避坑指南**：如果填地址时报错，请确保你的 **邮编 (Zip Code)** 和 **城市 (City)** 是严格对应的。国内卡请直接选 `China` 并填真实账单地址拼音。
    *   **费用说明**：别担心，只要在额度内（10GB），Cloudflare 绝对不会扣你一分钱。

## 📦 第二阶段：搭建保险箱 (Create Bucket)

进门后，你需要创建一个存放图片的“容器”。

1.  点击 **`Create Bucket`**。
2.  **起名**：比如 `my-image-box`（只能用小写字母和连字符）。
3.  **选位置**：选 `Automatic` 即可，它会自动选离你最近的机房。

## 🪟 第三阶段：点亮橱窗 (Public Access) —— **最容易漏掉的一步**

默认情况下，你的保险箱是不透光的，外网看不见图片。

1.  进入你刚建好的 Bucket，点击顶部的 **`Settings`** (设置)。
2.  向下翻找到 **`Public Development URL`**。
3.  **点亮它**：点击蓝色的 **`Enable`**。
4.  你会得到一个类似 `https://pub-xxx.r2.dev` 的网址，这就是你图片的**户口所在地**。

## 🔐 第四阶段：配一把全自动钥匙 (API Tokens)

为了让 Python 脚本或第三方工具能自动帮你搬运图片，你需要配一把钥匙。

1.  回到 R2 概览页，点击右侧的 **`Manage R2 API Tokens`**。
2.  点击 **`Create API token`**：
    *   **权限**：选 **`Object Read & Write`**。
    *   **有效期**：选 **`Forever`**。
3.  **保存密钥**：你会得到 **Access Key ID** 和 **Secret Access Key**。
    *   **警告**：Secret Key 只会出现这一次，一定要抄好！

---

## 🤖 第五阶段：接入 Antigravity OS 自动化引擎

如果你在使用 Antigravity OS 同步脚本，只需在 `.env` 文件里填入上述信息：

```bash
R2_ACCOUNT_ID="你的账户ID"
R2_ACCESS_KEY_ID="你的钥匙ID"
R2_SECRET_ACCESS_KEY="你的机密钥匙"
R2_BUCKET_NAME="你的桶名"
R2_PUBLIC_DOMAIN="你的.r2.dev网址"
```

### 🌟 运行后的黑科技效果：
*   **拖拽即上传**：你在 Obsidian 里拖一张原图叫 `我的生活.jpg`。
*   **全自动重命名**：脚本自动把它洗白成 `wo-de-sheng-huo.jpg` 并推送到云端。
*   **全自动替换**：本地笔记里的引用，瞬间变成全球可访问的 CDN 链接。

---

## 🏆 总结：为什么选 R2？
*   **大厂出品**：不用担心像小众图床那样突然关停。
*   **完全免费**：10GB 足够承载几千张高清照片。
*   **数据主权**：所有图片都在你自家的 Bucket 里，你可以随时批量下载。

---
#public