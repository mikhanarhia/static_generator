
import unittest

from src.markdownblock import block_to_block_type, markdown_to_blocks
from src.markdowntohtml import block_to_html_node, markdown_to_html, par_children, text_to_children
from src.splitter import text_to_textnodes
from src.textnode import text_node_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_awal(self):
        md = """
        # Ini heading 1 dengan **boldbold** text _itaitalic_


        ## heading kedua


        - ini ul 1
        - ini ul 2

        1. ol pertama
        2. ol kedua

        >apa aja boleh
        >quote pake spasi

        parag line 1
        parag line 2

        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """
        html = markdown_to_blocks(md)
        html_cek = html[5]
        res = markdown_to_html(md)
        # blocktype_in_html_cek = block_to_block_type(html_cek)
        # text_nodes_html_cek = text_to_textnodes(html_cek)
        # children_cek = text_node_to_html_node(text_nodes_html_cek[1])
        b = text_to_children(html_cek)
        c = block_to_html_node(html_cek)
        print(html_cek)
        print(b)
        print(par_children(b))
        # print(blocktype_in_html_cek)
        # print(text_nodes_html_cek)

        # print(res.to_html())
        expected = "<div><h1># Ini heading 1 dengan <b>boldbold</b> text <i>itaitalic</i></h1><h2>## heading kedua</h2><ul><li>ini ul 1</li><li>ini ul 2</li></ul><ol><li>ol pertama</li><li>ol kedua</li></ol><blockquote>apa aja boleh<br>quote pake spasi</blockquote><p>parag line 1 parag line 2</p><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(res.to_html(), expected)
