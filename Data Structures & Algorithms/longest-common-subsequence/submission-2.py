class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if text1[i] == text2[j]:
                cache[(i,j)] = 1 + dfs(i+1,j+1)
            else:
                cache[(i,j)] = max(dfs(i+1,j), dfs(i,j+1))
            
            return cache[(i,j)]
        
        return dfs(0,0)


        # What are we doing here,
        # when match then will do daigonal

        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
       

        t1, t2 = len(text1), len(text2)

        for i in range(t1-1,-1,-1):
            for j in range(t2-1,-1,-1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]  
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])

        return dp[0][0]