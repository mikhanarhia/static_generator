
import unittest

from src.markdownblock import block_to_block_type, markdown_to_blocks
from src.markdowntohtml import block_to_html_node, markdown_to_html, text_to_children
from src.splitter import text_to_textnodes
from src.textnode import text_node_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_awal(self):
        md = """
        # Ini heading 1 dengan **boldbold** text _itaitalic_

        - ini ul 1
        - ini ul 2

        >apa aja boleh

        parag line 1
        parag line 2
        """
        html = markdown_to_blocks(md)
        html_cek = html[0]
        res = markdown_to_html(md)
        # blocktype_in_html_cek = block_to_block_type(html_cek)
        # text_nodes_html_cek = text_to_textnodes(html_cek)
        # children_cek = text_node_to_html_node(text_nodes_html_cek[1])
        b = text_to_children(html_cek)
        c = block_to_html_node(html_cek)
        print(html_cek)
        # print(blocktype_in_html_cek)
        # print(text_nodes_html_cek)
        print("----")
        print(res.to_html())
        print("----")
