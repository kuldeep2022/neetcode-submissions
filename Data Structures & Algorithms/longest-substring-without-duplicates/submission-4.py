class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        res = 0
        l = 0
        for r,v in enumerate(s):
            while v in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(v)
            res = max(res,r-l+1)
        return res


        
            