class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        ROWS,COLS = len(grid), len(grid[0])

        # We will find the fresh fruites and also we will add rotten fruites to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        # Now we will run multi BFS on grid, similar to walls and gates questions
        time = 0
        directions  = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r,c  = queue.popleft()
                # We will run BFS on all the 4 nei of the rotten fruit in order to make it rotten
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if(row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -=1
                        queue.append((row,col))
            time += 1
        
        return time if fresh < 1 else -1