def runLengthEncoding(string):
    count, i, output = 0, 0, ""
    while i < len(string):
        letter = string[i]
        while i < len(string) and count < 9 and string[i] == letter:
            count += 1
            i += 1
        output += str(count) + letter
        count = 0
    return output

