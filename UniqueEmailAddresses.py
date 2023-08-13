class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res, test = "", True
        my_hash, r = set(), 0
        for email in emails:
            while email[r] != "@":
                if email[r] == "+":
                    test = False
                if test:
                    if email[r] != ".":
                        res += email[r]
                r += 1
            while r < len(email):
                res += email[r]
                r += 1
            my_hash.add(res)
            res, test, r = "", True, 0
        return len(my_hash)
        
