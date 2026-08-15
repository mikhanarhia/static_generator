import unittest

from src.splitter import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link
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

#EXTRACT MARKDOWN
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdwon_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

#SPLIT IMAGE AND LINK

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
