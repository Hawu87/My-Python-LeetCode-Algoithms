class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(", "[", "{"}
        stack = []
        for item in s:
            if item in opening:
                stack.append(item)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if item == ")":
                    if current != "(":
                        return False
                if item == "]":
                    if current != "[":
                        return False
                if item == "}":
                    if current != "{":
                        return False
        if stack:
            return False
        return True