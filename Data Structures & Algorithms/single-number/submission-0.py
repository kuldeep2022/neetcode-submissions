class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # We are doing EX-OR operation
        for n in nums:
            res = n ^ res
        
        return res
        