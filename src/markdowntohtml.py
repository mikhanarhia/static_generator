

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.markdownblock import BlockType, block_to_block_type, markdown_to_blocks
from src.splitter import text_to_textnodes
from src.textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html(md: str):
    list_block: list[str] = markdown_to_blocks(md)
    html_child = []
    for block in list_block:
        html_child.append(block_to_html_node(block))
    return ParentNode("div", html_child)



def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes: list[LeafNode] = []
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        html_nodes.append(leaf_node)
    return html_nodes

def block_to_html_node(text: str):
    block_type = block_to_block_type(text)
    if block_type != BlockType.CODE:
        block_leafs = text_to_children(text)
        match block_type:
            case BlockType.HEADING:
                return ParentNode("h", block_leafs)
            case BlockType.QUOTE:
                return ParentNode("blockquote", block_leafs)
            case BlockType.ORDERED:
                return ParentNode("ol", block_leafs)
            case BlockType.UNORDERED:
                return ParentNode("ul", block_leafs)
            case BlockType.PARAGRAPH:
                return ParentNode("p", block_leafs)
