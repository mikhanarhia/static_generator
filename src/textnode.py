from enum import Enum

from htmlnode import LeafNode




class TextType(Enum):
    TEXT = "plain text"
    BOLD = "bold"
    ITALIC = "italic"
    IMAGE = "image"
    LINK = "link"
    CODE = "code"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        if not isinstance(value, TextNode):
            return NotImplemented

        return (self.text, self.text_type, self.url) == (value.text, value.text_type, value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, text_node.url)
        case TextType.IMAGE:
            return LeafNode("img", "",
                {
                    "src": text_node.url,
                    "alt": text_node.text,
                })
        case _:
            raise Exception("Invalid text type")
