class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        def helperFunction(arr,word):
            for i in word:
                op = (ord(i) - ord('a')) % 26
                arr[op] += 1
            return tuple(arr)
        hashMap = defaultdict(list)

        for i in strs:
            arr = [0] * 26
            res = helperFunction(arr,i)
            hashMap[res].append(i)
        
        for i in hashMap.values():
            result.append(i)
        
        return result
       

        

        