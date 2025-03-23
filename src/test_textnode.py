import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
#1 assert equality , letting url default to None
    def test_eq(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

#2 assert inequality by inserting texttype, and texttype by value
    def test_non_eq(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', '**Bold text**')
        self.assertNotEqual(node, node2)

#3 assert equality with url values provided
    def test_eq2(self):
        node = TextNode('this is a text node', TextType.BOLD, 'https://www.boot.dev')
        node2 = TextNode('this is a text node', TextType.BOLD, 'https://www.boot.dev')
        self.assertEqual(node, node2)

#4 assert inequality with url values provided differently
    def test_non_eq2(self):
        node = TextNode('this is a text node', TextType.BOLD, 'https://www.boot.dev')
        node2 = TextNode('this is a text node', TextType.BOLD, 'https://www.boot.com')
        self.assertNotEqual(node, node2)

#5 assert inequality when texttype property is different
    def test_non_eq3(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.ITALIC)
        self.assertNotEqual(node, node2)

#6 test if repr works as expected
    def test_repr(self):
        node = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual("TextNode(this is a text node, **Bold text**, None)", repr(node))

#7 assert inequality when text property is different
    def test_non_eq4(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node2', TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()