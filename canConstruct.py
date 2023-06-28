class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        for val in magazine:
            my_dict[val] = 1 + my_dict.get(val, 0)

        for val in ransomNote:
            if val not in my_dict:
                return False
            if my_dict[val] == 0:
                return False
            my_dict[val] -= 1
        
        return True