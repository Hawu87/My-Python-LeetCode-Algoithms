class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #create an array of 26 characters for both arrays
        charS1 = [0] * 26
        charS2 = [0] * 26
        #initialize the s1 array chars and the first len(s1) chars in s2 array
        for i in range(len(s1)):
            charS1[ord(s1[i]) - ord('a')] += 1
            charS2[ord(s2[i]) - ord('a')] += 1

        matches = 0 #variable that will be true if all 26 chars match

        #iterate 26 through both to check size of matches
        for i in range(26):
            if charS1[i] == charS2[i]:
                matches += 1
        l = 0
        #iterate a sliding window that checks the last char on 
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            #right pointer index we are currently at
            index = ord(s2[r]) - ord('a')
            charS2[index] += 1
            #increament by 1 if they match at right index
            if charS2[index] == charS1[index]:
                matches += 1
            #if that increamentation made it greater by 1 cancel it
            elif charS2[index] == charS1[index] + 1:
                matches -= 1

            #left pointer we are currently at
            index = ord(s2[l]) - ord('a')
            charS2[index] -= 1
            #increament by 1 if they match at left index
            if charS2[index] == charS1[index]:
                matches += 1
            #if that increamentation made it greater by 1 cancel it
            elif charS2[index] == charS1[index]  - 1 :
                matches -= 1
            l += 1

        return matches == 26


                
                
