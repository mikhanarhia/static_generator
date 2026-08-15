


import re


from src.textnode import TextNode, TextType


def split_nodes_delimiter(nodes:list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    res = []
    for node in nodes:
        if node.text_type is not TextType.TEXT:
            res.append(node)
            continue

        temps = node.text.split(delimiter)
        if len(temps) % 2 == 0:
            raise Exception("there is no closing delimiter")

        for n, text in enumerate(temps):
            if text == "":
                continue
            if n % 2 != 0:
                res.append(TextNode(text, text_type))
            else:
                res.append(TextNode(text, TextType.TEXT))
    return res

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
           res.append(old_node)

        matches = extract_markdown_images(old_node.text)
        if matches == []:
            continue

        for match in matches:
            temp = old_node.text.split(f"![{match[0]}]({match[1]})", 1)
            if temp[0] != "":
                res.append(TextNode(temp[0], TextType.TEXT))
            res.append(TextNode(match[0], TextType.IMAGE, match[1]))
            old_node.text = temp[1]
    return res

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            res.append(old_node)

        matches = extract_markdown_links(old_node.text)
        if matches == []:
            continue

        for match in matches:
            temp = old_node.text.split(f"[{match[0]}]({match[1]})", 1)
            if temp[0] != "":
                res.append(TextNode(temp[0], TextType.TEXT))
            res.append(TextNode(match[0], TextType.LINK, match[1]))
            old_node.text = temp[1]
    return res

        ## TextNode("isi dari link", TextType.LINK, {"a":"b", "c": "d"})


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
