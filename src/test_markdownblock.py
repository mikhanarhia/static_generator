

import unittest

from markdownblock import BlockType, block_to_block_type, markdown_to_blocks


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

    #Test block_to_block_type
    def test_heading_1(self):
        text = "# heading1"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_heading_2(self):
        text = "## heading2"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_heading_3(self):
        text = "### heading3"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_heading_4(self):
        text = "#### heading4"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_heading_5(self):
        text = "##### heading5"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_heading_6(self):
        text = "###### heading6"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text), expected)

    def test_code(self):
        text = "```testing code```"
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(text), expected)

    def test_quote(self):
        text = ">. quotess"
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(text), expected)

    def test_unordered(self):
        text = "- blablabla"
        expected = BlockType.UNORDERED
        self.assertEqual(block_to_block_type(text), expected)

    def test_ordered(self):
        text = "1. blablabla"
        expected = BlockType.ORDERED
        self.assertEqual(block_to_block_type(text), expected)

    def test_paragraph_normal(self):
        text = "blabla"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(text), expected)

    def test_paragraph_heading_error(self):
        text = "###heading"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(text), expected)

    def test_paragraph_code_error(self):
        text = "```code``"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(text), expected)

    def test_paragraph_unordered_error(self):
        text = "-asf"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(text), expected)
