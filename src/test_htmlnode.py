import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
#1 test if no props inserted creates a node
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1,node2)

#2 test if HTMLNode with values given matches the expected representation
    def test_eq2(self):
        node = HTMLNode('test value', 'test tag')
        self.assertEqual(node.__repr__(),"HTMLNode(test value, test tag, None, None)")

#3 testing props_to_html functionality
    def test_eq3(self):
        node = HTMLNode('test value', 'test tag', props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')