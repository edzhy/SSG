class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ""
        for i,j in self.props.items():
            str += f' {i}="{j}"'
        return str
    
    def __repr__(self):
        tag, value, children, props = str(self.tag),str(self.value),str(self.children),str(self.props)
        return f"HTMLNode({tag}, {value}, {children}, {props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            ,self.value == other.value
            ,self.children == other.children
            ,self.props == other.props
        )
        
        
        
        