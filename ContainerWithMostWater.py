class Solution:
    def maxArea(self, height: List[int]) -> int:
        #create the left and the right pointers
        left, result, right = 0, 0, len(height) - 1
        #loop the list while left < right
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(area, result)
            #if the height of left is greater so decrement right
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result
