class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create set to hold unique values
        my_set= set()
        #maximum, left and right pointers
        maximum, left, right = 0, 0, 0
        while right < len(s):
            #if there is now repeatition, removing all letters from set
            # before repition occurance using left pointer
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            #appending elements to set
            my_set.add(s[right])
            #updating longest
            maximum = max(maximum, right - left + 1)
            right += 1
        
        return maximum