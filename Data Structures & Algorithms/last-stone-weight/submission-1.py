class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Intution is clear that we need to query 2 heaviest stones in every turn
        '''

        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap,-1 * s)
        
        while len(maxHeap) > 1:
            s1 = -1 * heapq.heappop(maxHeap)
            s2 = -1 * heapq.heappop(maxHeap)

            diff = s1 - s2
            heapq.heappush(maxHeap, -1 * diff)

        
        return -1 * heapq.heappop(maxHeap) if maxHeap[0] != 0 else 0

        