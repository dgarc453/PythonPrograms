def palindromeStr(number):
    return str(number) == (str(number))[::-1]


def palindromeInt(number):
    dig = 0
    reverse = 0
    if number < 0:
        number = abs(number)

    num = number

    while num > 0:
        digit = num % 10
        reverse = (reverse*10) + digit
        num = int(num/10)

    return reverse == number


# print(palindromeStr(122))
print(palindromeInt(121))
