import unittest
from text_to_textnode import text_to_textnodes
from textnode import *

class TestTextToTextNode(unittest.TestCase):
#1 testing the full functionality
    def test_full(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test_list = [TextNode(text, TextType.TEXT),]
        result = text_to_textnodes(test_list)
        self.assertListEqual(
            result,
                [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                ]
        )   
#2 testing adjacent inline elements
    def test_adjacent(self):
        test_list = [TextNode("Just checking if **big bold meets**_italic text from heaven_", TextType.TEXT),]
        result = text_to_textnodes(test_list)
        self.assertListEqual(result,
                             [TextNode("Just checking if ", TextType.TEXT),
                            TextNode("big bold meets", TextType.BOLD),
                            TextNode("italic text from heaven", TextType.ITALIC)]
                             )
#3 testing just text
    def test_just_text(self):
        test_list = [TextNode("Just checking if nothing really happens", TextType.TEXT),]
        result = text_to_textnodes(test_list)
        self.assertListEqual(result,
                             [TextNode("Just checking if nothing really happens", TextType.TEXT)]
                             )