class Solution:
    """
    Input: nums = [1,2,3,4,5], val = 3
    Output: [6,9,12]
    Explanation: Your function should return an array of the sum of the subarrays of size k
    """

    def removeElement(self, nums: List[int], val: int) -> List[int]:
        subarray_sum = sum(nums[:k])
        output = [subarray_sum]
        for i in range(1, len(nums) - k + 1):
            subarray_sum -= nums[i-1]
            subarray_sum += nums[i + k - 1]

            output.append(subarray_sum)

        return output