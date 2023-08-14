class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap, l = {}, {}, 0
        while l < len(s):
            charS, charT = s[l], t[l]
               
            if ((charS in sMap and sMap[charS] != charT) or
                (charT in tMap and tMap[charT] != charS)):
                return False
            
            sMap[charS] = charT
            tMap[charT] = charS
            l += 1
        return True
