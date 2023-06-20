class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating dictionary to hold the values, and the number of times they appear
        my_dict = {}
        #create 2D list, where the number of times something appears will be stored as the index
        #and then the items that appear that many times will be in an list
        output = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            my_dict[i] = 1 + my_dict.get(i, 0)
        
        for val, index in my_dict.items():
            output[index].append(val)
        result = []
        #loop from behind adding the terms to result array up until getting to k times
        for i in range(len(output) - 1, -1, -1):
            for b in output[i]:
                result.append(b)
                if len(result) == k:
                    return result