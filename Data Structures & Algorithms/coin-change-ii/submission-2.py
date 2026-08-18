class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # let's solve this using recursion
        # T- O(m*n) and S-O(n*m)
        cache = {}

        def dfs(i,a):
            if a == amount:
                return 1
            
            if a > amount:
                return 0
            
            if i == len(coins):
                return 0
            
            if (i,a) in cache:
                return cache[(i,a)]
            
            cache[(i,a)] = (dfs(i+1,a) + dfs(i, a + coins[i]))

            return cache[(i,a)]
        
        return dfs(0,0)

       