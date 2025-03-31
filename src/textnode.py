from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = 'normal text'
    BOLD = '**Bold text**'
    ITALIC = '_Italic text_' 
    CODE = '`Code text`'
    LINK = 'Link, in this format: [anchor text](url)'
    IMAGE = 'Image, in this format: ![alt text](url)'

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,TextNode):
        return (
            (self.text == TextNode.text) and
            (self.text_type == TextNode.text_type) and
            (self.url == TextNode.url)
        )
    def __repr__(self):
        text, text_type, url = str(self.text), str(self.text_type.value), str(self.url)
        return f'TextNode({text}, {text_type}, {url})'
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text, tag=None)  # Explicit None for plain text
        case TextType.BOLD:
            return LeafNode(value=text_node.text, tag='b')
        case TextType.ITALIC:
            return LeafNode(value=text_node.text, tag='i')
        case TextType.CODE:
            return LeafNode(value=text_node.text, tag='code')
        case TextType.LINK:
            return LeafNode(value=text_node.text, tag='a', props={'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode(value='', tag="img", props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise ValueError(f"Invalid TextType: {text_node.text_type}")