def checkingCommon(index, letter, strsLeft):
    listLetter = ""
    flag = False
    for ele in strsLeft:
        if index < len(ele):
            if ele[index] == letter:
                flag = True
            else:
                flag = False
        else:
            flag = False

    return flag


def longestCommonPrefix(strs):
    strs.sort()
    length = len(strs)
    strsLeft = strs[1:]
    element = ""
    for index, character in enumerate(strs[0]):
        flag = checkingCommon(index, character, strsLeft)
        if flag == True:
            element += character
        if flag == False:
            break

    return element


print(longestCommonPrefix(["dog", "racecar", "car"]))
