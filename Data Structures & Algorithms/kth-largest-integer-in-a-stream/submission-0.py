class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for n in nums:
            heapq.heappush(self.nums,-1 * n)
        

        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-1 * val)
        res = []
        i = 0
        while i < self.k:
            ele = heapq.heappop(self.nums)
            res.append(ele)
            i+=1
        ans = -1 * res[-1]
        for i in res:
            heapq.heappush(self.nums,i)
            
        return ans

        
