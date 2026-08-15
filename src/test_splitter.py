import unittest

from src.splitter import split_nodes_delimiter
from src.textnode import TextNode, TextType


class TestSplitter(unittest.TestCase):
    def test_split_nodes_delimiter_ITALIC(self):
        nodes = [TextNode("abcd efgh _jkl_ mno", TextType.TEXT)]
        list = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(list[0],TextNode("abcd efgh ", TextType.TEXT))
        self.assertEqual(list[1], TextNode("jkl", TextType.ITALIC))

    def test_split_nodes_delimiter_BOLD(self):
        nodes = [TextNode("abcd efgh **jkl** mno", TextType.TEXT)]
        list = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(list[0],TextNode("abcd efgh ", TextType.TEXT))
        self.assertEqual(list[1], TextNode("jkl", TextType.BOLD))

    def test_split_nodes_delimiter_double(self):
        nodes = [TextNode("abcd efgh **jkl** mno **pqr**", TextType.TEXT)]
        list = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(list[0],TextNode("abcd efgh ", TextType.TEXT))
        self.assertEqual(list[3], TextNode("pqr", TextType.BOLD))
