import unittest

from htmlnode import HTMLNode



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
