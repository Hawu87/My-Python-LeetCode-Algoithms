class Solution:
    """
    Given a binary array nums, 
    return the maximum number of consecutive 1's in the array.
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three 
    digits are consecutive 1s. The maximum number of 
    consecutive 1s is 3.

    Input: nums = [1,0,1,1,0,1]
    Output: 2
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest, current = 0, 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
        return max(current, longest)
