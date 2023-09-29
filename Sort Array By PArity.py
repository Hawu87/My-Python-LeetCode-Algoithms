class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #create a new array of size
        i, j = 0, len(nums) - 1
        
        #using left and right pointers
        while i < j:
            #loop till you find odd number
            while i < j and nums[i] % 2 == 0:
                i += 1
            #loop till you find even number
            while i < j and nums[j] % 2 == 1:
                j -= 1
            
            #swap the two
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums
