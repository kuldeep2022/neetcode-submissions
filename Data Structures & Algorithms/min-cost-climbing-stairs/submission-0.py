class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #[1,2,3] + [0]
        cost.append(0)
        n = len(cost)

        for i in range(n-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        
        # print(cost)
        return min(cost[0],cost[1])

        