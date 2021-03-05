

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        prev = self.getRow(rowIndex-1)
        array = [1]*(rowIndex+1)

        for i in range(1, rowIndex):
            array[i] = prev[i] + prev[i-1]
            
        return array