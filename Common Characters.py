def commonCharacters(strings):
    my_hash = {}
    for i in strings:
        curr = set(i)
        for letter in curr:
            my_hash[letter] = 1 + my_hash.get(letter, 0)
    output = []
    for char, count in my_hash.items():
        if count == len(strings):
            output.append(char)

    return output
        
        
        
        
        
