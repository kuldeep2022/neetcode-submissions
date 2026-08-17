class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        curSum = 0
        res = 0
        for i in nums:
            curSum += i

            if curSum == k:
                res+=1
            
            res+= d[curSum-k]

            d[curSum] += 1
        
        return res