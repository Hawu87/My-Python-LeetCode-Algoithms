class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #have a flag variable. It will start as zero, it will dertermine the direction
        #of the array, -1 means mono decreasing, +1 means mono increase
        #so it will declare once a direction is established

        flag = 0

        for i in range(1, len(nums)):
            #monotonic increasing
            if nums[i] < nums[i-1]:
                #declare direction to be increasing
                if flag == 0:
                    flag = 1
                #if direction changes then return false
                elif flag == -1:
                    return False
            
            #monotonic decreasing
            elif nums[i] > nums[i-1]:
                #declare direction to be decreasing
                if flag == 0:
                    flag = -1
                #if direction changes then return false
                elif flag == 1:
                    return False
        return True
        
        
