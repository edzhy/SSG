import unittest
from block_types import BlockType, block_line_check, block_to_block_type, is_ordered_list

class TestBlockType(unittest.TestCase):
#1 test if basic text comes out as paragraph
    def test_para(self):
        block = 'this is just a basic text'
        self.assertEqual(BlockType.paragraph, block_to_block_type(block))
        
#2 test for heading
    def test_head(self):
        block = '###### this might be the smallest heading I have ever seen!'
        self.assertEqual(BlockType.heading, block_to_block_type(block))

#3 test for code
    def test_code(self):
        block = '``` this might be the smallest heading I have ever seen```'
        self.assertEqual(BlockType.code, block_to_block_type(block))

#4 test for quote
    def test_quote(self):
        block = """>this might
>be the quotest
>block of all time"""
        self.assertEqual(BlockType.quote, block_to_block_type(block))

#5 test for unordered list
    def test_unorder(self):
        block = """- this might
- be the messiest
- list ever"""
        self.assertEqual(BlockType.unordered_list, block_to_block_type(block))

#6 test for unordered list
    def test_order(self):
        block = """1. this might
2. be the tidiest
3. list ever"""
        self.assertEqual(BlockType.ordered_list, block_to_block_type(block))

