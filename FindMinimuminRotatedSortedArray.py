class Solution:
    def findMin(self, nums: List[int]) -> int:
        #check the leftmost item in the array, compare it against the center
        #use two pointer to check portion of subarray
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            #if the middle is greater than the leftmost want to check right side
            if nums[m] >= nums[l]:
                l = m + 1
            #if the middle is less than the leftmost want to check right side
            else:
                r = m - 1
        return res
