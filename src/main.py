import os
import shutil
from textnode import TextNode, TextType
from copy_static import copy_static
from generate_page import extract_title, generate_page
from config import TARGET_DIR, WORKING_DIR


def main():
    target_dir = os.path.abspath(TARGET_DIR)
    working_dir = os.path.abspath(WORKING_DIR)

    if os.path.exists(target_dir): # check if path exist and delete anything in it
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path) # delete files
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path) # delete subdirectories
            except Exception as e:
                return f'Error: {e}'

    if not os.path.exists(target_dir): # if not exists create path
        try:
            os.mkdir(target_dir)
        except Exception as e:
            return f'Error: {e}'

    copy_static(target_dir, working_dir)
    generate_page("content/index.md", "template.html", "public/index.html")

main()