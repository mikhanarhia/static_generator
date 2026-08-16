

from enum import Enum


class BlockType(Enum):
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED = "unordered list block"
    ORDERED = "ordered list block"
    PARAGRAPH = "paragraph block"

def markdown_to_blocks(text: str) -> list[str]:
    list = text.split("\n\n")
    res = []
    for line in list:
        if line == "":
            continue
        if "\n" in line:
            temp = line.split("\n")
            for j, word in enumerate(temp):

                temp[j] = word.strip()
            line = "\n".join(temp)
        else:
            line = line.strip()
        line = line.strip("\n")
        res.append(line)
    return res

def block_to_block_type(text: str) -> BlockType:
    if text[:2] == "# " or text[:3] == "## " or text[:4] == "### " or text[:5] == "#### " or text[:6] == "##### " or text[:7] == "###### ":
        return BlockType.HEADING
    elif text[:3] == "```" and text[-3:] == "```":
        return BlockType.CODE
    elif text[0] == ">":
        return BlockType.QUOTE
    elif text[:2] == "- ":
       return BlockType.UNORDERED
    elif text[:3] == "1. ":
        return BlockType.ORDERED
    return BlockType.PARAGRAPH
