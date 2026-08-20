

import unittest

from main import extract_title
from src.markdowntohtml import block_to_html_node, markdown_to_html, text_to_children, ul_ol_block_children
from src.splitter import text_to_textnodes
from src.markdownblock import block_to_block_type, markdown_to_blocks
from src.textnode import text_node_to_html_node


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = """
        paragraf

        # heading1

        ## heading2"""
        self.assertEqual(extract_title(md), "heading1")

    def test_image_link(self):
        md = """
        # Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien

        ## Blog posts

        - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
        - [Why Tom Bombadil Was a Mistake](/blog/tom)
        - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

        ## Reasons I like Tolkien

        - You can spend years studying the legendarium and still not understand its depths
        - It can be enjoyed by children and adults alike
        - Disney _didn't ruin it_ (okay, but Amazon might have)
        - It created an entirely new genre of fantasy

        ## My favorite characters (in order)

        1. Gandalf
        2. Bilbo
        3. Sam
        4. Glorfindel
        5. Galadriel
        6. Elrond
        7. Thorin
        8. Sauron
        9. Aragorn

        Here's what `elflang` looks like (the perfect coding language):

        ```
        func main(){
            fmt.Println("Aiya, Ambar!")
        }
        ```

        Want to get in touch? [Contact me here](/contact).

        This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).

        """
        blocks = markdown_to_blocks(md)
        cek = blocks[5]
        print(cek)

        ul_list = ul_ol_block_children(cek)
        print(ul_list[0])
        print(ul_list[0].to_html())
        # print(markdown_to_html(cek).to_html())
