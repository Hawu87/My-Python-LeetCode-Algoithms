def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        for i in s:
            if not (i.isalnum()):
                s = s.replace(i, "")
        return s == s[::-1]



        
