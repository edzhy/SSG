import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_parent_node_with_none_tag(self):
        # This test passes if ParentNode raises a ValueError when tag is None
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "some content")]).to_html()
    # Test very deep nesting
    def test_deep_nesting(self):
        node = LeafNode("span", "deeply nested")
        for _ in range(10):  # Create 10 levels of nesting
            node = ParentNode("div", [node])
        # Assert expected HTML output
        self.assertEqual(node.to_html(),
                         '<div><div><div><div><div><div><div><div><div><div><span>deeply nested</span></div></div></div></div></div></div></div></div></div></div>')
    def test_basic_lesson_example(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(node.to_html(),
                         '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    def test_mixed_child_types(self):
        # Test parent with mixed child types
        leaf_child = LeafNode("b", "leaf content")
        parent_child = ParentNode("div", [LeafNode("span", "nested content")])
        mixed_parent = ParentNode("section", [leaf_child, parent_child])
        # Assert expected HTML output
        self.assertEqual(mixed_parent.to_html(),
                         '<section><b>leaf content</b><div><span>nested content</span></div></section>')