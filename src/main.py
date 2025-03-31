from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    #dummy = TextNode('this is some anchor text for the link', TextType.LINK, 'https://www.boot.dev')
    #print(dummy.__repr__())
    
    node = LeafNode("span", "deeply nested")
    for _ in range(10):  # Create 10 levels of nesting
        node = ParentNode("div", [node])
    print(node.to_html())
    leaf_child = LeafNode("b", "leaf content")
    parent_child = ParentNode("div", [LeafNode("span", "nested content")])
    mixed_parent = ParentNode("section", [leaf_child, parent_child])
    print(mixed_parent.to_html())
    print('------NEW TEST-------')
    node = TextNode("link to boot.dev", TextType.IMAGE, 'boot.dev')
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

if __name__ == "__main__":
    main()