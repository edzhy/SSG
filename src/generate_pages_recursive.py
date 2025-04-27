import os
from path_finder import path_finder
from file_copy import target_path_builder
import shutil
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        all_paths = path_finder(dir_path_content)
        dir_paths, md_paths = [], {}
        for path in all_paths:
            target_path = target_path_builder(dir_path_content, dest_dir_path, path)
            if os.path.isdir(path):
                dir_paths.append(target_path)
            elif os.path.isfile(path):
                if path.endswith('.md'):
                    html_target = target_path.replace('.md', '.html')
                    md_paths[path] = html_target
        for target_dir in dir_paths:
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
        for obj_src, obj_tgt in md_paths.items():
            generate_page(obj_src,template_path,obj_tgt)
    else:
        raise Exception('Invalid content directory, does not exist')
    return