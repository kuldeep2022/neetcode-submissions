class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        res = 0
        maxFreq = 0
        for r in range(len(s)):
            c = s[r]
            d[c] = d.get(c,0)+ 1
            maxFreq = max(maxFreq,d[c])

            while (r-l+1) - maxFreq > k:
                d[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
        
        return res


        