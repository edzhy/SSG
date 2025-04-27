#TARGET
#/Users/edgar/workspace/github.com/edzhy/SSG/public
#SOURCE
#/Users/edgar/workspace/github.com/edzhy/SSG/static
import os
import shutil
from path_finder import path_finder
def file_copy(source_dir, target_dir):
    if os.path.exists(target_dir):
        #deletes the test dir, and all its contents
        shutil.rmtree(target_dir)
        #recreates the target dir, for working solution should be switched to ../public
        os.mkdir(target_dir)
    else:
        raise Exception('Invalid target directory, does not exist')
    if os.path.exists(source_dir):
        all_paths = path_finder(source_dir)
        file_paths = {}
        for path in all_paths:
            target_path = target_path_builder(source_dir, target_dir, path)
            if os.path.isdir(path):
                os.mkdir(target_path)
            elif os.path.isfile(path):
                file_paths[path] = target_path
        
        for source_path, target_path in file_paths.items():
            shutil.copy(source_path, target_path)
    else:
        raise Exception('Invalid source directory, does not exist')

    return

def target_path_builder(source_dir, target_dir, obj_path):
    obj_relative_path = obj_path.removeprefix(source_dir)
    obj_absolute_target_path = target_dir + obj_relative_path
    return obj_absolute_target_path
