#This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
from split_nodes_img_link import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_by_all_delimiters
from textnode import *

def text_to_textnodes(md_text_nodes):
    
    
    md_text_nodes = split_nodes_image(md_text_nodes)
    md_text_nodes = split_nodes_link(md_text_nodes)
    md_text_nodes = split_nodes_by_all_delimiters(md_text_nodes)
    return md_text_nodes

#node = [TextNode('This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)', TextType.TEXT)]
#print(text_to_textnodes(node))

