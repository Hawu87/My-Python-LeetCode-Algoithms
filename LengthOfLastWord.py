def lengthOfLastWord(s):
    """Input string, and return the length of the last number.
    >>> lengthOfLastWord("Hello World")
    5
    >>> lengthOfLastWord("   fly me   to   the moon  ")
    4
    >>> lengthOfLastWord("luffy is still joyboy")
    6
    """
    if len(s) == 0:
        return 0
    total, num = 0, -1
    s = s.rstrip()
    while s[num] != " ":
        total += 1
        if len(s) + num == 0:
            break
        num -= 1
    return total