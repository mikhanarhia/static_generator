class HTMLNode:
    def __init__(self, tag: str | None, value: str | None, children: list["HTMLNode"] | None, props: dict | None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
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
