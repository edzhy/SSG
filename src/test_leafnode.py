import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
#1 test example from the lesson
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#2 test a LeafNode with some props given
    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

#3 test an image 
    def test_leaf_to_html_img(self):
        # Image tags typically have src attribute and sometimes alt, width, height, etc.
        props = {
            "src": "https://example.com/image.jpg",
            "alt": "Example image",
            "width": "300",
            "height": "200",
            "class": "featured-image"
        }
        # Image tags typically have empty value
        node = LeafNode("img", "", props)
        expected = '<img src="https://example.com/image.jpg" alt="Example image" width="300" height="200" class="featured-image"></img>'
        self.assertEqual(node.to_html(), expected)

#4 test node without a tag
    def test_no_tag(self):
        node = LeafNode(None, 'just simple value')
        self.assertEqual(node.to_html(), 'just simple value')