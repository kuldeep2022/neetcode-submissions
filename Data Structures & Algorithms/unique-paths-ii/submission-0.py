class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid),len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        

        def dfs(r,c, memo):

            if (r,c) in memo:
                return memo[(r,c)]
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            if r >=ROWS or c >=COLS or obstacleGrid[r][c] == 1:
                return 0
            
            memo[(r,c)] = (dfs(r+1,c,memo) + dfs(r,c+1,memo))

            return memo[(r,c)]

        return dfs(0,0,{})
        