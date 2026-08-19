

import argparse
import os
import shutil

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

if __name__ == "__main__":
    main()
