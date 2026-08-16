class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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