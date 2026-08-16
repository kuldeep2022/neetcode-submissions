class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0
        while r<len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)
            r+=1
        
        return maxp
        
        