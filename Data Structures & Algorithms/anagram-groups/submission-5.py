class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        def findCommonAnagrams(s):
            k = [0] * 26
            for c in s:
                 a = ord('z') - ord(c)
                 k[a] += 1
            t = tuple(k)
            if t in h:
                h[t].append(s)
            else:
                h[t] = [s]
        
        for i in strs:
            findCommonAnagrams(i)
        
        res = []
        for v in h.values():
            res.append(v)
        return res




        

        