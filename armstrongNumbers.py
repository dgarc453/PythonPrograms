def armstrongStr(number):
    total = 0
    numStr = str(number)
    n = len(numStr)
    if n == 0:
        return True
    for x in range(0, n):
        total += (pow(int(numStr[x]), n))

    return total == number


def numDigits(number):
    number = abs(number)
    counter = 0
    listNum = list()

    while number > 0:
        counter += 1
        listNum.append(number % 10)
        number = int(number/10)

    # print(counter)

    return counter, listNum[::-1]


def armstrongInt(number):
    if number == 0:
        return True

    power, listNum = numDigits(number)
    total = 0

    for ele in listNum:
        # print(ele)
        total += pow(ele, power)

    return total == number


# print(armstrongStr(1253))

print(armstrongInt(1534))
