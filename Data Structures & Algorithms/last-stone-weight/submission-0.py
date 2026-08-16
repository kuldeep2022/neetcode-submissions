class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap,-1 * s)
        
        while len(heap)> 1:
            l1  = -1 * heapq.heappop(heap)
            l2 = -1 * heapq.heappop(heap)
            newrock = l1 - l2
            heapq.heappush(heap,-1 * newrock)
        
        return -1 * heap[0] if heap[0] != 0 else 0


        