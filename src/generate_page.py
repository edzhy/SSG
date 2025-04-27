from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
def generate_page(from_path, template_path, dest_path):
    dest_path_info = dest_path.split('/')
    target_dir = dest_path_info[0] + '/'
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file:
        md_content = file.read()
    with open(template_path, 'r') as file:
        html_template = file.read()
    html_body_node = markdown_to_html_node(md_content).to_html()
    h1_heading = extract_title(md_content)
    html_template_w_title = html_template.replace("{{ Title }}", h1_heading)
    html_full = html_template_w_title.replace("{{ Content }}", html_body_node)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    with open(dest_path, 'w') as target_file:
        target_file.write(html_full)
    return