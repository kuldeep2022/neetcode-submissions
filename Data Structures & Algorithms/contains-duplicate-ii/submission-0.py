class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i,v in enumerate(nums):
            if v not in d:
                d[v] = []
            d[v].append(i)
        
        print(d)
        for _,v in d.items():
            if len(v) >= 2:
                for i in range(1,len(v)):
                    if abs(v[i] - v[i-1]) <= k:
                        return True

        return False



        