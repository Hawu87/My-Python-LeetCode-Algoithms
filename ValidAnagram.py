class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of 
    a different word or phrase, typically using all the original letters exactly once.
    
    Input: s = "anagram", t = "nagaram"
    Output: true

    Input: s = "rat", t = "car"
    Output: false
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = {}
        for val in s:
            if val not in my_dict:
                my_dict[val] = 1
            else:
                my_dict[val] += 1

        for i in t:
            if i not in my_dict:
                return False
            else:
                if my_dict[i] == 0:
                    return False
                my_dict[i] -= 1
        
        return True