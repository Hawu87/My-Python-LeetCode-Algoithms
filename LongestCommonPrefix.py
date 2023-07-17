class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Example 1:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        Example 2: 
        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        """
        strs.sort()
        output = ""
        a = strs[0]
        b = strs[-1]
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                break
            output += a[i]
        return output
