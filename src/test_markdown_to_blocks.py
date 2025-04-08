import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
#1 testing basic functionality of markdown blocks
    def test_markdown_blocks(self):

        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
#2 test tabs and spaces at the begining and end of blocks
    def test_spacing(self):
        md = """
    A tab before a block

 A space before and after. 

 A space before and after the first line. 
Which should not be cleared as it is part of the block.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "A tab before a block",
                "A space before and after.",
                "A space before and after the first line. \nWhich should not be cleared as it is part of the block."
            ],
        )
#3 test to see empty blocks don't show up
    def test_empty_block(self):
        md = """
What a **wonderful** day! 




    Let's do _IT_ :) 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         [
                             "What a **wonderful** day!",
                             "Let's do _IT_ :)"
                         ]
                         )