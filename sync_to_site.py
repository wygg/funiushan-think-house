import os
import shutil

# 定义源目录与目标目录
SOURCE_DIR = "/Users/wygg/mycode/myAntigravity/400-projects/410-agile-design/202603-momo-mountain-house-renovation"
TARGET_DIR = "/Users/wygg/mycode/myAntigravity/930-public-buffer/momo-mountain-house-website/src/content/docs/01-建造实录"

if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)
os.makedirs(TARGET_DIR)

def copy_with_frontmatter(src_path, dest_path, default_title=""):
    if not os.path.exists(src_path):
        return
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 如果已经有 frontmatter，就不重复添加
    if content.startswith("---\n"):
        with open(dest_path, "w", encoding="utf-8") as fw:
            fw.write(content)
        return

    # 从首行提取 # H1 标题
    title = default_title
    first_line = content.split('\n')[0]
    if first_line.startswith("# "):
        title = first_line.replace("# ", "").strip()
    
    # 包装双引号，避免特殊符号破坏 YAML
    title_escaped = title.replace('"', '\\"')
    frontmatter = f'---\ntitle: "{title_escaped}"\n---\n\n'
    
    with open(dest_path, "w", encoding="utf-8") as fw:
        fw.write(frontmatter + content)

# 物理拷贝各个工段目录到分类中
for item in os.listdir(SOURCE_DIR):
    item_path = os.path.join(SOURCE_DIR, item)
    if os.path.isdir(item_path):
        readme_path = os.path.join(item_path, "README.md")
        if os.path.exists(readme_path):
            target_sub_dir = os.path.join(TARGET_DIR, item)
            os.makedirs(target_sub_dir, exist_ok=True)
            default_t = item.split("-", 1)[-1].replace("-", " ").title() if "-" in item else item
            copy_with_frontmatter(readme_path, os.path.join(target_sub_dir, "index.md"), default_t)

# 处理大根目录文章与作战图 (直接放入 src/content/docs)
docs_root = os.path.join(TARGET_DIR, "..")
copy_with_frontmatter(os.path.join(SOURCE_DIR, "README.md"), os.path.join(docs_root, "000-项目哲学.md"), "项目哲学")
copy_with_frontmatter(os.path.join(SOURCE_DIR, "00-project-cockpit/01-planning-and-budget/000-全周期装修施工流程图.md"), os.path.join(docs_root, "000-全周期施工导航.md"), "全周期施工导航")

print("✅ 所有文档已成功打上 Astro 所需的 YAML Frontmatter, 并同步完毕！")
