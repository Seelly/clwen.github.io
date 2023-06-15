import os
import glob

# 获取当前目录
current_dir = os.getcwd()

# 获取所有md文件路径
md_files = glob.glob(os.path.join(current_dir, "**/*.md"), recursive=True)

# 遍历每个md文件，生成对应的markdown链接
for md_file in md_files:
    # 获取相对于当前目录的文件路径，用于生成markdown链接
    relative_path = "/"+os.path.relpath(md_file, current_dir).replace('\\', '/')
    # 获取文件名（不包含扩展名）
    file_name = os.path.splitext(os.path.basename(md_file))[0]
    # 生成markdown链接
    markdown_link = f"- [{file_name}]({relative_path})"
    print(markdown_link)
