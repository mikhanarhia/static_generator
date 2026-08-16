

import unittest

from markdownblock import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        block = markdown_to_blocks(md)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertListEqual(block, expected)

    def test_multiple_newlines(self):
        md = """
        line 1




        line 2



        line 3
        line 4
        """
        block = markdown_to_blocks(md)
        expected = [
            "line 1",
            "line 2",
            "line 3\nline 4",
        ]
        self.assertListEqual(block, expected)
