class HTMLNode:
    def __init__(self, tag: str | None, value: str | None, children: list["HTMLNode"] | None = None, props: dict | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplemented

    def props_to_html(self) -> str:
        if self.props is None or "":
            return ""
        string = ""
        for key, value in self.props.items():
            string += f" {key}='{value}'"

        return string[1:]

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value},\n{self.children},\n{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict | None = None) -> None:
        super().__init__(tag, value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("value is missing")

        if self.tag == None:
            return self.value

        prop_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                prop_string += f" {key}='{value}'"

        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value},\n{self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict | None = None) -> None:
        super().__init__(tag, value = None, children = children, props = props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("tag is missing")
        if self.children == None:
            raise ValueError("children is missing")

        cat = ""
        for child in self.children:
            cat += child.to_html()


        return f"<{self.tag}{self.props_to_html()}>{cat}</{self.tag}>"
