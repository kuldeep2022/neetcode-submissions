class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0

        def helper(l,r):
            nonlocal res,resLength
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > resLength:
                    res = s[l:r+1]
                    resLength = r-l+1
                l-=1
                r+=1
            return res


        for i in range(len(s)):
            # odd length
            l,r = i,i
            helper(l,r)
            
            # even length
            l,r = i,i+1
            helper(l,r)
        
        return res
        