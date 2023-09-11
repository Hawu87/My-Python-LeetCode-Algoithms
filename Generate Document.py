def generateDocument(characters, document):
    # Write your code here.
    charMap = {}
    for i in characters:
        charMap[i] = 1 + charMap.get(i, 0)

    for i in document:
        if i not in charMap:
            return False
        if charMap[i] == 0:
            return False
        charMap[i] -= 1
    return True
