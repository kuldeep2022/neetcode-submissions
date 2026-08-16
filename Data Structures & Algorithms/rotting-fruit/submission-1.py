class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # First let's find rotten orages places and total number of fresh oranges
        fresh = 0
        queue = deque([])
        ROWS, COLS = len(grid),len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        print(queue, fresh)
        time = 0
        direct = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dc, dr in direct:
                    row, col = r+dr, c+dc
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        fresh -=1
                        grid[row][col] = 2
                        queue.append((row,col))
            
            time += 1

        return time if fresh == 0 else -1


