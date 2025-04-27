from generate_page import generate_page
from file_copy import file_copy
from generate_pages_recursive import generate_pages_recursive
import sys
def main():
    basepath = '/'
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    file_copy('/Users/edgar/workspace/github.com/edzhy/SSG/static','/Users/edgar/workspace/github.com/edzhy/SSG/docs')
    dir_path_content = 'content/'
    template_path = 'template.html'
    dest_dir_path = 'docs/'
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)
if __name__ == "__main__":
    main()