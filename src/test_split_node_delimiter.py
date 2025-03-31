import unittest
from textnode import text_node_to_html_node, TextNode, TextType
from split_delimiter import split_nodes_delimiter, split_nodes_by_all_delimiters

class TestSplitNodeDelimiter(unittest.TestCase):
#1 test to check out this madness
    def test_code_block(self):
        nodes = [TextNode("This is text with a `code block` word. ", TextType.TEXT),
                TextNode("This is text with a _italic block_ word. ", TextType.TEXT),
                TextNode("This is text with a **bold block** word. ", TextType.TEXT)]
        nodes = split_nodes_by_all_delimiters(nodes)
        final = ''
        for node in nodes:
            final += (text_node_to_html_node(node).to_html())
        self.assertEqual(final,
            "This is text with a <code>code block</code> word. This is text with a <i>italic block</i> word. This is text with a <b>bold block</b> word. ")
#2 test with multiple delimiters in same text
    def test_multiple(self):
        nodes = [TextNode("This is text with a `code block` word and a _italic block_. ", TextType.TEXT),
                TextNode("This is text with a _italic block_ with a **bold word**.", TextType.TEXT)]
        nodes = split_nodes_by_all_delimiters(nodes)
        final = ''
        for node in nodes:
            final += (text_node_to_html_node(node).to_html())
        self.assertEqual(final,
        "This is text with a <code>code block</code> word and a <i>italic block</i>. This is text with a <i>italic block</i> with a <b>bold word</b>.")
#3 test with invalid delimiters
    def test_failure(self):
        node = [TextNode("This is a **bold test** with a failure **syntax.",TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_by_all_delimiters(node)       
#4 test with no delimiters
    def test_no_deli(self):
        nodes = [TextNode('simple dimple text',TextType.TEXT)]
        nodes = split_nodes_by_all_delimiters(nodes)
        self.assertEqual(nodes,
        [TextNode('simple dimple text',TextType.TEXT)])
#5 test with adjacent code block backticks
    def test_double_backticks(self):
        nodes = [TextNode('simple dimple `` test with `code`.',TextType.TEXT)]
        nodes = split_nodes_by_all_delimiters(nodes)
        final =''
        for node in nodes:
            final += (text_node_to_html_node(node).to_html())
        self.assertEqual(final,
        "simple dimple <code></code> test with <code>code</code>.")