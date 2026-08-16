import unittest
from src.splitter import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_eq(self):
        node = TextNode("this", TextType.BOLD)
        node2 = TextNode("that", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_url_is_none(self):
        node = TextNode("this", TextType.TEXT)
        self.assertIsNone(node.url)

#TEXT NODE TO HTMLNODE
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("isi dari link", TextType.LINK, {"a":"b", "c": "d"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "isi dari link")
        self.assertEqual(html_node.to_html(), "<a a='b' c='d'>isi dari link</a>")

    def test_code(self):
        node = TextNode("a code line", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>a code line</code>")

    def test_img(self):
        node = TextNode("alt textnya", TextType.IMAGE, "www.bruh.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), "<img src='www.bruh.com' alt='alt textnya'></img>")



if __name__ == "__main__":
    unittest.main()
