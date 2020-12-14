def gettingChar(word):
    letter = list()
    for character in word:
        if character not in letter:
            letter.append(character)

    letter.sort()
    return letter


def gettingNumChar(word, letter):
    mydict = list()
    for ele in letter:
        mydict.append(word.count(ele))
    return mydict


def anagrams(word, words):

    letter = gettingChar(word)

    numCharWord1 = gettingNumChar(word, letter)
    numCharWord2 = list()

    resultList = list()

    for word2 in words:
        if len(word) == len(word2):
            numCharWord2 = gettingNumChar(word2, letter)
            if numCharWord2 == numCharWord1:
                resultList.append(word2)

    return resultList


anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
