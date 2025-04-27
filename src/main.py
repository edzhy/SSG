from generate_page import generate_page
from file_copy import file_copy
def main():
    file_copy('/Users/edgar/workspace/github.com/edzhy/SSG/static','/Users/edgar/workspace/github.com/edzhy/SSG/public')
    generate_page('content/index.md','template.html','public/index.html')
if __name__ == "__main__":
    main()