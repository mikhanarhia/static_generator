import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):


    def test_tag(self):
        tag = "<a>"
        value = "bruh"
        children = None
        props = {
            "a": "bruh",
            "b": "bruh bruh",
        }
        node = HTMLNode(tag, value, children, props)
        self.assertIs(node.tag, "<a>")

    def test_props_to_html(self):
        tag = "<a>"
        value = "bruh"
        children = None
        props = {
            "a": "bruh",
            "b": "bruh bruh",
        }
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(node.props_to_html(),"a='bruh' b='bruh bruh'")

    def test_repr(self):
        tag = "<a>"
        value = "bruh"
        children = None
        props = {
            "a": "bruh",
            "b": "bruh bruh",
        }
        node = HTMLNode(tag, value, children, props)
        self.assertIsNone(node.children)

#LEAF TEST

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "bruh", {"bruh": "www.bruh.com"})
        self.assertEqual(node.to_html(), "<a bruh='www.bruh.com'>bruh</a>")

#PARENT TEST

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
