class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}

        def helper(s):
            chrMap = [0] * 26
            for c in s:
                indexVal = ord('z') - ord(c)
                chrMap[indexVal] += 1
            
            hKey = tuple(chrMap)
            if hKey in hMap:
                hMap[hKey].append(s)
            else:
                hMap[hKey] = [s]

        for i,v in enumerate(strs):
            helper(v)
            
        
        return list(hMap.values())




        

        