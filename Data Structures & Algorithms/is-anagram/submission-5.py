class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1,h2 = {}, {}

        for v1,v2 in zip(s,t):
            h1[v1] = h1.get(v1,0) + 1
            h2[v2] = h2.get(v2,0) + 1
        
        return h1 == h2


        