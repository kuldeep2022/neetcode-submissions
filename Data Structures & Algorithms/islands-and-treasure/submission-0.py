class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        # We will do multipoint BFS
        #Let's add all the gates in our queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    #We are adding this gates to visit set so we don't need to visit it again
                    visit.add((r,c))
        
        def addRoom(r,c):
            if r < 0 or r >= ROWS or c<0 or c>= COLS or (r,c) in visit or grid[r][c] == -1:
                return
            q.append((r,c))
            visit.add((r,c))
        

        # Now we have all the gates added in our queue
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
            
                # Let's add nei of the gates
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)

            # Increment the distance after adding nei of gates
            dist += 1