import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        h = {}
        for i in nums:
            h[i] = h.get(i,0)+1

        for key,v in h.items():
            heapq.heappush(heap,(-1*v,key))
        res = []
        while k>0:
            q = heapq.heappop(heap)
            res.append(q[1])
            k-=1
        return res
            