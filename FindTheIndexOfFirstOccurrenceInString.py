class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if len(needle) > len(haystack):
            return -1
        gap = len(haystack) - len(needle)
        for i in range(gap + 1):
            if haystack[i] == needle[0]:
                flag = True
                index, z = i, 1
                i += 1
                while z < len(needle):
                    if haystack[i] == needle[z]:
                        z += 1
                        i += 1
                    else:
                        flag = False
                        break
                if flag:
                    return index
        return -1
        