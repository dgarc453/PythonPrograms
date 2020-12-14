def alphabet_position(text):

    text = text.lower()
    valueStr = ""
    for char in range(0, len(text)):
        if text[char] != " ":
            value = ord(text[char]) - 96
            if value > 0 and value < 27:
                valueStr += str(value) + " "

    return valueStr[:-1]


alphabet_position("The sunset sets at twelve o' clock.")
