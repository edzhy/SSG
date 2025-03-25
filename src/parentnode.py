from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if not self.children:
            raise ValueError("Children cannot be empty for ParentNode")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}>{children_html}</{self.tag}>"
        
    #create __eq__ method for this call
    def __eq__(self, ParentNode):
        return (
            (self.tag == ParentNode.tag) and
            (self.children == ParentNode.children) and
            (self.props == ParentNode.props)
        )
    #create __repr__ method
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'