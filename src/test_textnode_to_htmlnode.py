import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextN2HTMLN(unittest.TestCase):
#1 test case with basic textnode
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")   
#2 test case with tag value and text
    def test_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node")
#3 test case with tag value and text
    def test_italic_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a text node")
#4 test case with tag, value and props
    def test_url_text(self):
        node = TextNode("link to boot.dev", TextType.LINK, 'boot.dev')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "link to boot.dev")
        self.assertEqual(html_node.props, {'href': 'boot.dev'})
#5 test case with tag, value and props
    def test_image_text(self):
        node = TextNode("image of Boots", TextType.IMAGE, 'boot.dev')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="boot.dev" alt="image of Boots"></img>')
#6 test case with tag, value and props
    def test_error_raising(self):
        node = TextNode("fake text", 'TEST')       
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)