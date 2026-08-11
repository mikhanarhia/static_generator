from enum import Enum




class TextType(Enum):
    PLAIN = "plain text"
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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
