def aVeryBigSum(ar):
    sum = 0

    for ele in ar:
        sum = sum + ele

    return sum


print(aVeryBigSum([1000000001, 1000000002,
                   1000000003, 1000000004, 1000000005]))
