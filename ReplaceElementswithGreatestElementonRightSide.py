class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [0] * len(arr)
        max_term = -1
        i = len(arr) - 1
        while i >= 0:
            output[i] = max_term
            max_term = max(max_term, arr[i])
            i -= 1
        return output
