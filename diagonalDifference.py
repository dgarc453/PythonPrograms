def diagonalDifference(arr):

    sum_left_right = 0
    sum_right_left = 0
    for index, ele in enumerate(arr):
        sum_left_right = sum_left_right + ele[index]

    # print(sum_left_right)
    newList = array(list(reversed(arr)))
    print(type(newList))
    # for index, ele in reversed(list(enumerate(arr))):

    # print(sum_right_left)

    total = sum_left_right + sum_right_left
    if total < 0:
        total = abs(total)

    print(total)
    return arr


diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
# output 15
