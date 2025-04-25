#/Users/edgar/workspace/github.com/edzhy/SSG/public
import os
import shutil
def file_copy(source_dir, target_dir):
    if os.path.exists(target_dir):
        print(target_dir)
        shutil.rmtree('/Users/edgar/workspace/github.com/edzhy/SSG/public/test')
        os.mkdir('/Users/edgar/workspace/github.com/edzhy/SSG/public/test')
    else:
        print('nope')
    return

source_dir = input('source directory: ')
target_dir = input('target directory: ')
file_copy(source_dir, target_dir)