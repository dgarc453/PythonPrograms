def compareTriplets(a, b):
    returnArray = [0, 0]
    for i in range(0, 3):
        # print(i)
        # print(a[i])
        # print(b[i])
        if a[i] == b[i]:
            print("Equal")
            pass
        elif a[i] > b[i]:
            # print("a > b")
            # print("{} > {}".format(a[i], b[i]))
            returnArray[0] = returnArray[0] + 1
        elif a[i] < b[i]:
            print("{} > {}".format(a[i], b[i]))
            returnArray[1] = returnArray[1] + 1

    return returnArray


compareTriplets([4, 8, 1], [3, 6, 8])
