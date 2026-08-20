

import argparse
import os
import shutil

from src.markdownblock import BlockType, block_to_block_type, markdown_to_blocks
from src.markdowntohtml import heading_children, markdown_to_html

def main():
    # parser = argparse.ArgumentParser(description="Source Directory to Copy")
    # parser.add_argument("dir", help="The name of the directory to copy in the current directory")
    # args = parser.parse_args()
    list_files = list_all_files("static")

    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    for file in list_files:
        copy_file = file.split("/")
        if len(copy_file) > 2:
            file_path = file.split("/")
            req_dir = file_path[1:-1]
            req_dir = "public/" + "/".join(req_dir)
            os.makedirs(req_dir, exist_ok=True)
            shutil.copy(file, os.path.join(req_dir, copy_file[-1]))
        else:
            shutil.copy(file, os.path.join("public", copy_file[-1]))

    generate_page("content/index.md", "template.html", "public/index.html")


def list_all_files(source: str) -> list[str]:
    if not os.path.exists(source):
        raise Exception("source dir didn't exist in the current directory")

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

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content_md = f.read()
    with open(template_path, "r") as f:
        content_template = f.read()
    html_content = markdown_to_html(content_md)
    html_title = extract_title(content_md)
    full_html = content_template.replace("{{ Title }}", html_title)
    full_html = full_html.replace("{{ Content }}", html_content.to_html())

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)



if __name__ == "__main__":
    main()
