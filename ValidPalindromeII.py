class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                delL, delR = s[l + 1: r + 1], s[l: r]
                return (delL == delL[::-1] or delR == delR[::-1])
            l, r = l + 1, r -1
        return True
