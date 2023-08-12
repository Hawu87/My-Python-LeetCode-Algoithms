class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1]
        for _ in range(rowIndex):
            temp = [0] + output + [0]
            row = []
            for i in range(len(temp) - 1):
                row.append(temp[i] + temp[i + 1])
            output = row
        return output
