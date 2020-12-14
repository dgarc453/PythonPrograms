def romanToInt(s):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    value = 0
    prev = 0
    for character in s:
        current = dict[character]
        if prev < current:
            value += current - 2*prev
        else:
            value += current
        prev = current


romanToInt("IX")
