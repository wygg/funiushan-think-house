---
date: 2026-02-20
description: 一份给新手的傻瓜式保姆级教程，教你如何在 Obsidian 中实现在当前文件夹一键新建笔记、弹出互动窗口填写标题/Tag，并完美遵守操作系统的全英文自动重命名“宪法”。本文附带详细配置截图。
publish:
- Garden
tags:
- System/SOP
- Obsidian
- Templater
- AI-Echo
title: 🚀 Obsidian x Templater：互动式纯净文章生成流程 (SOP)
---

# 🚀 Obsidian x Templater：互动式纯净文章生成流程 (SOP)

当你建立了一个庞大而严谨的知识库（如 Antigravity OS），你一定希望自己每次写日记或研究笔记时，**不需要手动去改复杂的文件名、不需要复制粘贴排版、更不会让新笔记不听话地乱跑到处飞**。

本教程将教你打造一个绝妙的心流（Flow）：**随手一按 ➡️ 在当前正在看的文件夹里新建空壳 ➡️ 弹出精美的窗口问你叫什么 ➡️ 瞬间生成带时间戳标准命名的全套笔记。**

---

## 🛠️ 步骤一：扎实基本盘（Obsidian 防原形毕露设置）

首先，为了防止你的新文件和随手粘贴的图片“不受控制地掉到走廊上（根目录）”，我们需要修改 Obsidian 的地基设置。

1. 打开 Obsidian 左下角的 **「设置」**（或者按键盘 `Cmd + ,`）。
2. 在左侧菜单找到 **「文件与链接 (Files and Links)」**。
3. **关键修改 A**：找到「新建笔记的存放位置 (Default location for new notes)」，下拉选择为 👉 **「当前文件所在的文件夹 (Same folder as current file)」**。
   * *(这保证了你看着谁，谁的旁边就会生出新笔记，绝对不乱跑。)*
4. **关键修改 B**：找到「附件默认存放路径 (Default location for new attachments)」，下拉选择为 👉 **「在指定的文件夹下 (In the folder specified below)」**，然后在弹出的选项中设定为你系统专属的附件黑洞（例如 `900-system/950-attachments`）。
   * *(这保证了你不小心粘贴的截图绝不会弄脏你的日记目录。)*
   ![Screenshot 2026-02-20 at 8.13.31 PM.png](https://pub-de21be1de01e413e8fddf6e380989c0a.r2.dev/screenshot-2026-02-20-at-8-13-31-pm.jpg)

---

## 🛠️ 步骤二：放置魔法法术（安装并配置模板）

我们需要依赖一个名叫 **Templater** 的强大第三方插件（它比 Obsidian 自带的模板引擎强大几百倍）。

1. 去「第三方插件 (Community plugins)」里下载并启用 **Templater**。
2. 找到你的系统专门装模板的文件夹（例如 `900-system/940-templates/`），在这个文件夹里建一个名为 `Constitution_Article_Template.md` 的笔记。
3. **将下面的“符咒”（代码）原封不动地复制粘贴进去：**

```markdown
\<%*
// 提示用户输入所需信息
let title = await tp.system.prompt("文章中文标题 (Title):");
let tagsInput = await tp.system.prompt("文章标签 (逗号分隔, 例如: Life, AI, Reading):");

// 防呆设计：如果不输入标题直接关掉，那就中止魔法
if (title === null || title.trim() === "") {
    new Notice("未输入标题，模板已中止！");
    return;
}

// 防呆设计：自动洗白你手误打出的“中文逗号”
let tagsList = [];
if (tagsInput !== null && tagsInput.trim() !== "") {
    tagsList = tagsInput
        .replace(/，/g, ',')
        .split(',')
        .map(tag => tag.trim())
        .filter(tag => tag !== "");
}

// 提取精准系统时间
let fullDateTime = tp.date.now("YYYY-MM-DD HH:mm:ss");
let dateStr = tp.date.now("YYYY-MM-DD");
let timestampStr = tp.date.now("YYYYMMDDHHmm");

// 自动生成符合 Kebab-Case 机器友好的文件名 (仅时间戳与英文短横，防止乱码)
let newFileName = `${timestampStr}-${title}`;

// 执行当前目录下的【原位安全重命名】
await tp.file.rename(newFileName);

// 此时根据机器标准重命名完毕，以下是展示给人类看的极其优雅的中文界面
_%>
---
title: <% title %>
date: <% dateStr %>
created: '<% fullDateTime %>'
tags: [<% tagsList.join(", ") %>]
description: 
---

# <% title %>

> [!abstract] 核心摘要
>

## 📌 记录与思考
<% tp.file.cursor(1) %>

---
#Garden <!-- 准许公开时，删去此行注释即可被脚本扫描发布 -->
```
*(注意第一行的 `\<%*` 是为了防止在这篇教程里被误触发加的反斜杠，复制到真实模板里时要把反斜杠去掉变为 `<%*` 。)*

---

## 🛠️ 步骤三：绑定一闪而过的快捷键（为魔法安上拉环）

法术有了，我们要把它绑在你最顺手的键盘按键上。

**图1：在设置中指明模板存放路径，并开启新文件级触发**
> *（请将你刚才截图的图1粘贴于此，展示 Template folder location 为 `900-system/940-templates`，且打开了 Trigger Templater on new file creation）*
![Screenshot 2026-02-20 at 8.12.46 PM.png](https://pub-de21be1de01e413e8fddf6e380989c0a.r2.dev/screenshot-2026-02-20-at-8-12-46-pm.jpg)

1. 进入「设置」-> 找到下方第三方插件的 **Templater** 的专属设置页。
2. 确保最上面 **Template folder location** 选对了你的模板文件夹。
3. 往下滚，找到 **Template Hotkeys (模板快捷键设置)**。

**图2：将宪法模板加入快速唤醒名单**
> *（请将你刚才截图的图2粘贴于此，展示出在 Template hotkeys 中搜索并选中 `Constitution_Article_Template.md` 加入快捷键列的步骤）*
![图2：Template Hotkeys 配置](image-not-found)
![Screenshot 2026-02-20 at 8.13.04 PM.png](https://pub-de21be1de01e413e8fddf6e380989c0a.r2.dev/screenshot-2026-02-20-at-8-13-04-pm.jpg)
4. 在 Template hotkeys 下的搜索框，把你刚才写的那个 `Constitution_Article_Template.md` 模板选上，然后点击旁边的 ➕ 号按钮。
   * *(至此它就被列入了待唤醒名单。)*

**图3：将 Insert 绑定为你的灵魂快捷键**
> *（请将你刚才截图的图3粘贴于此，展示出在系统快捷键里搜索该模板，并将 Insert 操作绑定为 `⌘ ⇧ I`，务必注意不要绑到 Create 操作上！）*
![图3：全局快捷键绑定 Insert 动作](image-not-found)
![Screenshot 2026-02-20 at 8.13.52 PM.png](https://pub-de21be1de01e413e8fddf6e380989c0a.r2.dev/screenshot-2026-02-20-at-8-13-52-pm.jpg)
5. 左侧菜单来到全局的 **「快捷键 (Hotkeys)」**。
6. 搜索：**`Templater: Insert Constitution_Article_Template`**。（注意是 **Insert**，千万不要选成 **Create**！只有 Insert 才能原汁原味保存在你的当前目录下）。
7. 点击它旁边的加号，按下你极度习惯的快捷键组合，例如：**`Cmd + Shift + I`** 绑定它！

---

## 🎯 终极享受篇：见证心流开启

所有配置只需做一次。做完之后，未来的每一天你的写作都会如同丝般顺滑：

1. **落点**：在左侧文件树，点到你想要写作的具体小抽屉（比如你的日记文件夹）。
2. **生胎**：按一下系统默认的新建键 `Cmd + N`（前提是你已经将新建日记落点设在了**当前所在文件夹**）。
3. **注魂**：趁光标还在这个“未命名”的空壳里绝望闪烁时，右手按下 **`Cmd + Shift + I`**。
4. **对话**：屏幕中间优雅弹出问卷框：“主人，标题叫什么？”。你输入《周末学习感悟》。再次弹出“标签是什么？”你输入：`阅读, 进化`。回车。
5. **降生**：魔法发生了。这个文件瞬间甩掉了沉睡的外衣，改名成坚不可摧的 `202602202015-周末学习感悟.md` 钉死在你的抽屉里，中间的文字瞬间排布起完美的 Markdown 双链网格，而光标恰好就停留在“记录与思考”的正文行。

请开启你的创造吧，OS 主理人。