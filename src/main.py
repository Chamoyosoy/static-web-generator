import os
import shutil
from copy_static import copy_static
from generate_page import generate_pages
from config import STATIC_DIR, CONTENT_DIR, TARGET_DIR, TEMPLATE


def main():
    static_dir = os.path.abspath(STATIC_DIR)
    content_dir = os.path.abspath(CONTENT_DIR)
    target_dir = os.path.abspath(TARGET_DIR)
    template = os.path.abspath(TEMPLATE)

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

    copy_static(static_dir, target_dir)
    generate_pages(content_dir, template, target_dir)

main()