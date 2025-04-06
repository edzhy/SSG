from textnode import *
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        old_text = old_node.text
        old_node_images = extract_markdown_images(old_text)
        #if no images detected, just end this iteration by adding all old_node content to result list as textnode
        if not old_node_images:
            result.append(TextNode(old_text, TextType.TEXT))
            continue
        #iterate over the list of tuples from extract_markdown_images function
        for alt_text, img_url in old_node_images:
            img_markdown = f"![{alt_text}]({img_url})"
            parts = old_text.split(img_markdown, 1)
            if len(parts[0]) > 0:
                result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, img_url))
            old_text = parts[1]
        if len(old_text) > 0:
            result.append(TextNode(old_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = [] 
    for old_node in old_nodes:
        old_text = old_node.text
        old_node_links = extract_markdown_links(old_text)
        #if no links detected, just end this iteration by adding all old_node content to result list as textnode
        if not old_node_links:
            result.append(TextNode(old_text, TextType.TEXT))
            continue
        #iterate over the list of tuples from extract_markdown_links function
        for link_text, link_url in old_node_links:
            link_markdown = f"[{link_text}]({link_url})"
            parts = old_text.split(link_markdown, 1)
            if len(parts[0]) > 0:
                result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, link_url))
            old_text = parts[1]
        if len(old_text) > 0:
            result.append(TextNode(old_text, TextType.TEXT))
    return result

#print(split_nodes_link([TextNode("test beginning [link 1 text](url/of/link1.com), link2 [text for link 2](url/of/link2.com) test end", TextType.TEXT), ]))
#print(split_nodes_image([TextNode("test beginning ![alt text for image](url/of/image.jpg), img2 ![alt text for 2 image](url/of/2image.jpg) test end", TextType.TEXT), ]))