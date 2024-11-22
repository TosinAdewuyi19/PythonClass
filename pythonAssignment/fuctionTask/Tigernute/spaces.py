def remove_spaces(string):
    result = ""
    for char in string:
        if char != " ":
            result += char
    return result

