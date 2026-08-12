import unittest

from htmlnode import HTMLNode, LeafNode



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
        self.assertEqual(node.to_html(), "<a> bruh='www.bruh.com'bruh</a>")
