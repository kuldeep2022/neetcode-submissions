class Solution:
    def trap(self, height: List[int]) -> int:
        left ,right = [],[]
        curMax = 0

        for i in range(len(height)):
            left.append(curMax)
            curMax = max(curMax,height[i])
        
        curMax = 0
        for i in range(len(height)-1,-1,-1):
            right.append(curMax)
            curMax = max(curMax,height[i])
        
        right.reverse()
        res = 0
        for i in range(len(height)):
            trap = min(left[i],right[i]) - height[i]
            if trap >= 0:
                res+=trap
        return res


        