class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        for i in my_dict:
            if my_dict[i] == 1:
                return i