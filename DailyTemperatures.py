class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack to keep track of values
        #pop value if temperature greater than that found
        #else append num
        #use a list of tuple to hold index and val
        stack = []
        output = [0] * len(temperatures)
        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                output[stack[-1][0]] = (index - stack[-1][0])
                stack.pop()
            stack.append((index, val))
        return output
        

