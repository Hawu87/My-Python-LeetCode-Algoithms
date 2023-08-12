class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for _ in range(numRows - 1):
            temp = [0] + output[-1] + [0]
            curr = []
            for j in range(len(temp) - 1):
                curr.append(temp[j] + temp[j + 1])
            output.append(curr)
        return output
