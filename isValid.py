def isValid(s):
    openP = 0
    closeP = 0
    openCB = 0
    closeCB = 0
    openB = 0
    closeB = 0

    print("HELLO")
    for character in s:
        print(character)
        if character == "(":
            openP += 1
        if character == ")":
            if openP == 0:
                return False
            else:
                closeP += 1
        if character == "[":
            openB += 1
        if character == "]":
            if openB == 0:
                return False
            else:
                closeB += 1
        if character == "{":
            openCB += 1
        if character == "}":
            if openCB == 0:
                return False
            else:
                closeCB += 1

    print("P open{} close{}".format(openP, closeP))
    print("B: open{} close{}".format(openB, closeB))
    print("CB: open{} close{}".format(openCB, closeCB))
    return openP == closeP and openB == closeB and openCB == closeCB


print(isValid(""))
