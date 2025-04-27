from generate_page import generate_page
from file_copy import file_copy
from generate_pages_recursive import generate_pages_recursive
def main():
    file_copy('/Users/edgar/workspace/github.com/edzhy/SSG/static','/Users/edgar/workspace/github.com/edzhy/SSG/public')
    #generate_page('content/index.md','template.html','public/index.html')
    dir_path_content = 'content/'
    template_path = 'template.html'
    dest_dir_path = 'public/'
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
if __name__ == "__main__":
    main()