class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(c,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            if c == n+1:
                return
            
            # Include
            comb.append(c)
            dfs(c+1,comb)
            comb.pop()

            # Not to include
            dfs(c+1,comb)
        
        dfs(1,[])
    
        return res