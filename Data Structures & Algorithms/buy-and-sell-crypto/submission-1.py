class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        There are some following conditions which I can think of :-
        1. if the current day price is > next day price let's start our window from second day
        2. if current day price is < next day price then we have a profit but we are still not sure if that is the max profit which we can get.
        '''
        if len(prices) < 2:
            return 0

        l,r = 0,1
        maxP = 0
        while r < len(prices):
            while r< len(prices)-1 and prices[l] >= prices[r]:
                l = r
                r+=1
            #print("R", r)
            maxP = max(maxP,prices[r] - prices[l])
            r+=1
        
        #print(maxP)
        return maxP
            
            
            
        