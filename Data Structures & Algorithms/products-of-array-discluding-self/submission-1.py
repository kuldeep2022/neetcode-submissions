class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1] * len(nums)
        postFix = 1
        for i in range(1,len(preFix)):
            preFix[i] = preFix[i-1]* nums[i-1]
 
        for i in range(len(nums)-1,-1,-1):
            preFix[i] *= postFix
            postFix *= nums[i]  
        

        return preFix

        
        