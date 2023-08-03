class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #loop through outer
        #do binary search within each row
        #check if our value lies between the end and start point
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            c = (l + r) // 2
            if target < matrix[m][c]:
                r = c - 1
            elif target > matrix[m][c]:
                l = c + 1
            else:
               return True
        return False
