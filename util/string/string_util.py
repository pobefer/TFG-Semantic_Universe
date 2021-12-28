def get_left_split(text, separator="@"):
    return text.split(separator)[0]


def get_right_split(text, separator="@"):
    return text.split(separator)[-1]
