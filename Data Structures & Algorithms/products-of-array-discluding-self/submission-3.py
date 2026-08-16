class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [1] * len(nums)
        postfixArray = [1] * len(nums)
        postfix = 1
        for i in range(1,len(nums)):
           prefixArray[i] = prefixArray[i-1] * nums[i-1]
       
        for i in range(len(nums)-1,-1,-1):
            prefixArray[i] *= postfix
            postfix *= nums[i]

        return prefixArray

        # for i in range(len(nums)-2,-1,-1):
        #     postfixArray[i] = postfixArray[i+1] * nums[i+1]
        # res = []
        # for p1,p2 in zip(prefixArray,postfixArray):
        #     res.append(p1*p2)
        



        
        