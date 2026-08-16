class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        There are some following conditions which I can think of :-
        1. if the current day price is > next day price let's start our window from second day
        2. if current day price is < next day price then we have a profit but we are still not sure if that is the max profit which we can get.
        '''
        maxProfit = 0
        if len(prices)<2:
            return maxProfit
        l = 0
        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l=r
            
            elif prices[l] < prices[r]:
                maxProfit = max(maxProfit,prices[r] - prices[l])
                
        
        return maxProfit

        

            
            
            
        