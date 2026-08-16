class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1,h2 = {}, {}

        for v1 in s:
            h1[v1] = h1.get(v1,0) + 1
        
        for v2 in t:
            h2[v2] = h2.get(v2,0) + 1
        
        
       # print("h1", h1,"h2", h2)
        for k in h1:
            if k not in h2 or h1[k] != h2[k]:
                return False
        
        return True


        