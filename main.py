


import os
import shutil
import sys

from src.markdownblock import BlockType, block_to_block_type, markdown_to_blocks
from src.markdowntohtml import heading_children, markdown_to_html


base = sys.argv
if len(base) == 2:
    basepath = base[1]
else:
    basepath = "/"


def main(basep = basepath):
    print(basep)
    static = "static"
    public = "docs"
    content = "content"
    template = "template.html"


    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)

    copy_file(static, public)

    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive(content, template, public, basep)

def copy_file(source: str, dest: str) -> None:
    if not os.path.exists(source):
        raise Exception(f"{source} doesn't exist")
    if not os.path.exists(dest):
        raise Exception(f"{dest} doesn't exist")

    list_files = list_all_files(source)

    for file in list_files:
        copy_file = file.split("/")
        if len(copy_file) > 2:
            file_path = file.split("/")
            req_dir = file_path[1:-1]
            req_dir = f"{dest}/" + "/".join(req_dir)
            os.makedirs(req_dir, exist_ok=True)
            shutil.copy(file, os.path.join(req_dir, copy_file[-1]))
        else:
            shutil.copy(file, os.path.join(dest, copy_file[-1]))

def list_all_files(source: str) -> list[str]:
    if not os.path.exists(source):
        raise Exception(f"{source} didn't exist in the current directory")

    res = []
    list_files = os.listdir(source)
    for file in list_files:
        file_dir = os.path.join(source, file)
        if os.path.isfile(file_dir):
           res.append(file_dir)
        else:
           res.extend(list_all_files(file_dir))
    return res

def extract_title(md: str) -> str:
    blocks = markdown_to_blocks(md)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is BlockType.HEADING and heading_children(block) == "h1":
                title = block.strip("#")
                return title.strip()
    raise Exception("no h1 header for title")

def generate_page(from_path: str, template_path: str, dest_path: str, basep = basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content_md = f.read()
    with open(template_path, "r") as f:
        content_template = f.read()
    html_content = markdown_to_html(content_md)
    html_title = extract_title(content_md)
    full_html = content_template.replace("{{ Title }}", html_title)
    full_html = full_html.replace("{{ Content }}", html_content.to_html())
    full_html = full_html.replace('href="/', f'href="{basep}')
    full_html = full_html.replace('src="/', f'src="{basep}')
    full_html = full_html.replace("href='/", f"href='{basep}")
    full_html = full_html.replace("src='/", f"src='{basep}")



    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basep = basepath) -> None:
    print(f"generating page from {dir_path_content} with {template_path} to {dest_dir_path}")
    if not os.path.exists(dir_path_content):
        raise Exception(f"source {dir_path_content} doesn't exist")
    if not os.path.exists(template_path):
        raise Exception(f"template {template_path} doens't exist")

    if os.path.isdir(dir_path_content):
        files = os.listdir(dir_path_content)
        for file in files:
            new_source = os.path.join(dir_path_content, file)
            new_dest = os.path.join(dest_dir_path, file)
            generate_pages_recursive(new_source, template_path, new_dest, basep)
    else:
        dest_dir_path = dest_dir_path.replace(".md", ".html")
        generate_page(dir_path_content, template_path, dest_dir_path, basep)


if __name__ == "__main__":
    main(basepath)
