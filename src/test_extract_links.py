import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class TestExtractLinks(unittest.TestCase):
#1 test an image extraction
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
#2 test a link extraction
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [anchor text for a link](https://www.boot.dev)"
        )
        self.assertListEqual([("anchor text for a link", "https://www.boot.dev")], matches)
#3 extract a link from text that also has image
    def test_extract_only_link(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and [anchor text for a link](https://www.boot.dev)"
        )
        self.assertListEqual([("anchor text for a link", "https://www.boot.dev")], matches)