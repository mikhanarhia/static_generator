


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
