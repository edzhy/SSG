import unittest
from markdown_to_html_node import markdown_to_html_node
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import *


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_complex_markdown(self):
        md = """# Main Heading

This is a paragraph with **bold text** and _italic text_ and `inline code`.

## Subheading

> This is a blockquote
> With multiple lines

- Unordered list item 1
- Unordered list item 2 with **bold** and `code`

1. Ordered list item 1
2. Ordered list item 2 with _italic_

```
def hello_world():
    print("Hello, **world**!")
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
    html,
    "<div><h1>Main Heading</h1><p>This is a paragraph with <b>bold text</b> and <i>italic text</i> and <code>inline code</code>.</p>" +
    "<h2>Subheading</h2><blockquote>This is a blockquote With multiple lines</blockquote>" +
    "<ul><li>Unordered list item 1</li><li>Unordered list item 2 with <b>bold</b> and <code>code</code></li></ul>" +
    "<ol><li>Ordered list item 1</li><li>Ordered list item 2 with <i>italic</i></li></ol>" +
    "<pre><code>def hello_world():\n    print(\"Hello, **world**!\")\n</code></pre></div>"
        )
