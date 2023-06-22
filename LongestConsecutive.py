class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maximum = 1
        my_set = set(nums)
        for val in my_set:
            if (val - 1) not in my_set:
                count = 1
                current = val + 1
                while current in my_set:
                    count += 1
                    current += 1
                maximum = max(maximum, count)
        return maximum