def reverse(x):
    if x <= -2**31 or x >= 2**31-1:
        return 0
    else:
        numStr = str(x)
        result = 0
        if x >= 0:
            reverse = numStr[::-1]
            result = int(reverse)
        else:
            numStr = numStr[1:]
            reverse = "-" + numStr[::-1]
            result = int(reverse)

        if result <= -2**31 or result >= 2**31-1:
            return 0

        return result


print(reverse(-123))
