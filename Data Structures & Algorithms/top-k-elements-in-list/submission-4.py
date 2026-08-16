import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for i,v in enumerate(nums):
            hMap[v] = hMap.get(v,0) + 1
        
        heap = []
        for key,v in hMap.items():
            heapq.heappush(heap,[(-1*v),key])
        res = []

        while k > 0:
            _,ans = heapq.heappop(heap)
            res.append(ans)
          
            k-=1
        
        return res