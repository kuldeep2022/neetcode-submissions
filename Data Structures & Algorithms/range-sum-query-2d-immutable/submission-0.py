class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixM = []
        for r in range(len(matrix)):
            pre = 0
            preR = []
            for c in range(len(matrix[0])):
                pre += matrix[r][c]
                preR.append(pre)
            self.prefixM.append(preR)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        maxC = max(col1,col2)
        minC = min(col1,col2)
        minR = min(row1,row2)
        maxR = max(row1,row2)
        res = 0
        for r in range(minR,maxR+1):
            if minC == 0:
                res+= self.prefixM[r][maxC]
            else:
                res+= self.prefixM[r][maxC] - self.prefixM[r][minC-1]
        
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)