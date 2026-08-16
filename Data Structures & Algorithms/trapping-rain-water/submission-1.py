class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l< r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] 
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] 
        
        return res


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


        