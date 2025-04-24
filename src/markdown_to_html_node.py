import re
from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from textnode import TextNode,TextType, text_node_to_html_node
from text_to_textnode import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode
#takes a full markdown document and converts into a single parent HTMLNode: ParentNode
def markdown_to_html_node(markdown):
    #blocks will have a list of pure markdown text blocks
    blocks = markdown_to_blocks(markdown)
    parentnode_list = []
    for block in blocks:
        textnode_list = []
        #this line will store the block type, in order to map it to corresponding HTMLNode: BlockType(Enum)
        block_type = block_to_block_type(block)
        heading = str()
        if block_type is BlockType.heading:
            heading = heading_tagger(block)
        #a function to strip the markdown blocks : strip_markdown(md, md_type)
        #from all md specific characters, so that remaining text could be fed into HTMLNode with proper tag
        block_text = strip_markdown(block, block_type)
        #the blocks text needs to be converted from text to TextNode via text_to_textnodes function
        if block_type is BlockType.code:
            code_child = text_node_to_html_node(TextNode(block_text, TextType.CODE))
            parentnode_list.append(ParentNode('pre',[code_child]))
            continue
        elif block_type in (BlockType.ordered_list, BlockType.unordered_list):
            list_items = block.split('\n')
            list_item_nodes = []
            
            for list_item in list_items:
                if list_item.strip():  # Skip empty lines
                    # Process the list item text (strip markers like "- " or "1. ")
                    # This depends on how your lists are formatted in markdown
                    if block_type is BlockType.ordered_list:
                        # Strip numbered prefix like "1. "
                        item_text = re.sub(r'^\d+\.\s+', '', list_item)
                    else:
                        # Strip unordered list marker "- "
                        item_text = re.sub(r'^[-]\s+', '', list_item)
                        
                    # Create TextNodes for the item text and convert to HTML nodes
                    item_html_nodes = text_to_children(item_text)
                    # Wrap in li tag
                    list_item_nodes.append(ParentNode('li', item_html_nodes))
            
            # Create ul or ol parent
            if block_type is BlockType.ordered_list:
                parentnode_list.append(ParentNode('ol', list_item_nodes))
            else:
                parentnode_list.append(ParentNode('ul', list_item_nodes))
            continue
        textnode_list.extend(text_to_textnodes([TextNode(block_text, TextType.TEXT)]))
        #text_node_to_html_node(text_node) will return LeafNodes
        leafnode_list = []
        for textnode_item in textnode_list:
            leafnode_list.append(text_node_to_html_node(textnode_item))
        #and the block needs to be parent node for all the return LeafNode children
        if block_type is BlockType.heading:
            parentnode_list.append(ParentNode(heading, leafnode_list))
        elif block_type is BlockType.quote:
            parentnode_list.append(ParentNode('blockquote', leafnode_list))
        else:
            parentnode_list.append(ParentNode('p', leafnode_list))
  
    #parent needs to capture all in enclosing <div> tags
    return ParentNode('div',parentnode_list)

def text_to_children(text):
    list_of_textnodes = text_to_textnodes([TextNode(text, TextType.TEXT)])
    resulting_children = []
    for textnode in list_of_textnodes:
        resulting_children.append(text_node_to_html_node(textnode))
    return resulting_children


def strip_markdown(md, md_type):
    #strips all block related special md characters and returns a string
    if md_type is BlockType.heading:
        return md.lstrip('# ')
    if md_type is BlockType.code:
        lines = md.split('\n')
        # Remove the first and last line (triple backticks)
        if lines[0].strip() == '```' and lines[-1].strip() == '```':
            return '\n'.join(lines[1:-1]) + '\n'
        return md
    if md_type is BlockType.quote:
        lines = md.split("\n")
        # Remove the "> " from the beginning of each line
        cleaned_lines = [line[2:] if line.startswith(("> ")) else line for line in lines]
        return " ".join(cleaned_lines)
    if md_type == BlockType.unordered_list:
        lines = md.split("\n")
        # Remove the "- " from the beginning of each line
        cleaned_lines = [line[2:] if line.startswith(("- ")) else line for line in lines]
        return "\n".join(cleaned_lines)
    elif md_type == BlockType.ordered_list:
        lines = md.split("\n")
        # Remove the "1. ", "2. ", etc. from the beginning of each line
        cleaned_lines = []
        for line in lines:
            # Find the first occurrence of ". " and remove everything before it plus the ". "
            if ". " in line:
                cleaned_lines.append(line[line.index(". ") + 2:])
            else:
                cleaned_lines.append(line)
        return "\n".join(cleaned_lines)
    if md_type is BlockType.paragraph:
        # Replace newlines with spaces and normalize whitespace
        return ' '.join(md.split())
    return md

def heading_tagger(md):
    counter = 0
    for character in md:
        if character == '#':
            counter += 1
            continue
        else: 
            break
    return f'h{counter}' 

