

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
                return ParentNode(heading_children(text), block_leafs)
            case BlockType.QUOTE:
                block_leafs[0].value = quote_children(block_leafs[0].value)
                return ParentNode("blockquote", block_leafs)
            case BlockType.ORDERED:
                return ParentNode("ol", ul_ol_block_children(text))
            case BlockType.UNORDERED:
                return ParentNode("ul", ul_ol_block_children(text))
            case BlockType.PARAGRAPH:
                return ParentNode("p", par_children(block_leafs))
    return ParentNode("pre", code_children(text) )

def ul_ol_block_children(text: str) -> list[ParentNode]:
    block_type = block_to_block_type(text)
    if block_type is BlockType.ORDERED:
        rep_num = 3
    else:
        rep_num = 2
    uls: list[str] = text.split("\n")
    ul_list: list[ParentNode] = []
    for ul in uls:
        ul = ul[rep_num:]
        each_line_nodes = text_to_children(ul)
        ul = ParentNode("li", each_line_nodes)
        ul_list.append(ul)
    return ul_list

def par_children(children: list[LeafNode]) -> list[LeafNode]:
    res: list[LeafNode] = []
    for child in children:
        if child.tag == None and child.value != None:
            child.value = child.value.replace("\n", " ")
        res.append(child)
    return res
    # par_lines = text.replace("\n", " ")
    # return [LeafNode(None, par_lines)]

def code_children(text: str) -> list[LeafNode]:
    return [LeafNode("code", text[3:-3])]

def heading_children(text: str) -> str:
    num_hashtag = text.split(" ", 1)
    match len(num_hashtag[0]):
        case 1:
            return "h1"
        case 2:
            return "h2"
        case 3:
            return "h3"
        case 4:
            return "h4"
        case 5:
            return "h5"
        case 6:
            return "h6"
        case _:
            raise Exception("# more than 6")

def quote_children(text: str) -> str:

    num_sign = text.split(" ", 1)

    if len(num_sign[0]) > 1:
        rep = ">"
    else:
        rep = "> "

    res = text.replace(rep, "")
    res = res.replace("\n", "<br>")
    return res
