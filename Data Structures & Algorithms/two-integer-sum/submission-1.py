class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i,v in enumerate(nums):
            remainder = target - v
            if v in h:
                return [h[v],i]
            h[remainder] = i
        
            
        