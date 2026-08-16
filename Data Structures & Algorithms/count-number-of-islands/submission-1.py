class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        '''
        Quick Note for Myself
        if interviewer allow me to change the value in grid then I can modify value to something else but not then I need to use visit set
        '''

        def dfs(r,c):
            if r<0 or c<0 or r == ROWS or c == COLS or grid[r][c] != "1":
                return
            
            grid[r][c] = 0
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r,c)
        
        return ans



        