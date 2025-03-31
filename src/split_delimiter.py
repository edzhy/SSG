from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type_p):
    result = []
    for old_node in old_nodes:
        if TextType.TEXT != old_node.text_type:
            result.append(old_node)
            continue
        
        count = old_node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception('The initial input contains invalid Markdown syntax')
        sub_nodes = old_node.text.split(delimiter)
        for i in range(1,len(sub_nodes)+1,1):
            if i % 2 == 1:
                result.append(TextNode(sub_nodes[i-1],text_type=TextType.TEXT))
            else:
                result.append(TextNode(sub_nodes[i-1],text_type=text_type_p))
    return result


def split_nodes_by_all_delimiters(old_nodes):
    """
    Process all supported delimiter types in sequence.
    The order matters - typically code, then bold, then italic.
    """
    text_type_dict = {
        TextType.CODE : '`',
        TextType.BOLD : '**',
        TextType.ITALIC : '_'
        }
    
    result = old_nodes
    for text_type, delimiter in text_type_dict.items():
        result = split_nodes_delimiter(result, delimiter, text_type)
    
    return result


