class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        d1,d2 = {},{}
        for i,j in zip(s,t):
            d1[i] = d1.get(i,0) + 1
            d2[j] = d2.get(j,0) + 1
        
        return d1 == d2
       


        