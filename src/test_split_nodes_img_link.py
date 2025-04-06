from textnode import *
from split_nodes_img_link import split_nodes_image, split_nodes_link
import unittest

class TestSplitImgLinks(unittest.TestCase):
#1 test for images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
#2 test for links
    def test_split_link(self):
        node = TextNode(
            "This is text with an [link](GOOGLE.COM) and another [second link](BOOT.DEV)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "GOOGLE.COM"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "BOOT.DEV"),
            ],
            new_nodes,
        )
#3 test where Text node starts off with a link, and ends with a link
    def test_split_link2(self):
        node = TextNode(
            "[link](GOOGLE.COM)This is text in the middle [second link](BOOT.DEV)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "GOOGLE.COM"),
                TextNode("This is text in the middle ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "BOOT.DEV"
                ),
            ],
            new_nodes,
        )
#4 test node that starts with an image, has another immediately
    def test_split_images2(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png) the end",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" the end", TextType.TEXT)
            ],
            new_nodes,
        )
#5 test with no images, that gets ran through function
    def test_split_nothing(self):
        node = TextNode(
            "totally boring text just to prove that both functions don't make any changes to it",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("totally boring text just to prove that both functions don't make any changes to it", TextType.TEXT)
            ],
            new_nodes,
        )
#6 test where there is a link and image, but only link function gets called
    def test_split_link3(self):
        node = TextNode(
            "![image](GOOGLE.COM)This is text in the middle [link](BOOT.DEV)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("![image](GOOGLE.COM)This is text in the middle ", TextType.TEXT),
                TextNode("link", TextType.LINK, "BOOT.DEV"),
            ],
            new_nodes,
        )