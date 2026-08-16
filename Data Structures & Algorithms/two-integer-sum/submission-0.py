class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,v in enumerate(nums):
            if v in hashMap:
                return [hashMap[v],i]
            remainder = target - v
            hashMap[remainder] = i
        
            
        