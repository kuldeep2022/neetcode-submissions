class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def helper(x,y):
            res = x**2 + y**2
            heapq.heappush(heap,[res, x,y])
        
        for x,y in points:
            helper(x,y)
        
        ans = []
        while k > 0:
            res,x,y = heapq.heappop(heap)
            ans.append([x,y])
            k-=1
        
        return ans

        