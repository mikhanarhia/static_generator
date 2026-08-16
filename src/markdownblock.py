

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
