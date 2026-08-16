class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1] * len(nums)
        postFix = [1] * len(nums)

        for i in range(1,len(preFix)):
            preFix[i] = preFix[i-1]* nums[i-1]
 

        for i in range(len(postFix)-2,-1,-1):
            postFix[i] = postFix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            postFix[i] = postFix[i] * preFix[i]
        

        return postFix

        
        