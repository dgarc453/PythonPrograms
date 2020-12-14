def twoSum(nums, target):
    seen = {}
    print(type(seen))
    for i, v in enumerate(nums):
        print('values:', i, v)
        remaining = target - v
        print('Remaining', remaining)
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
        print(seen)
    return []


numsList = [11, 22, 33, 44]
print(twoSum(numsList, 33))
