class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can be solved using Heap with T -> O(n*log k)
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)
        
        minHeap = []
        for key,v in hashMap.items():
            minHeap.append([-v,key])
        
        heapq.heapify(minHeap)
      
        res = []
        while k > 0:
          
            ans = heapq.heappop(minHeap)
            res.append(ans[1])
            k -=1
        
        return res

        