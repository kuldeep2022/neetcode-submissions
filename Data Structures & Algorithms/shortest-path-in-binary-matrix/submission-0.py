class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        N = len(grid)
        directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]]
        path = 0
        visit = set()
        visit.add((0,0))

        while queue:
            r,c,length = queue.popleft()

            if r == N-1 and c == N-1:
                return length
            
            for dr,dc in directions:
                nr, nc = dr+r, dc+c
                if (0<=nr<N and 0<=nc<N and grid[nr][nc] == 0 and (nr,nc) not in visit):
                    queue.append((nr,nc,length+1))
                    visit.add((nr,nc))
        
        return -1
