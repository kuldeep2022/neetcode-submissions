class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i,v in enumerate(nums):
            if v in hMap:
                return [hMap[v],i]
            compli = target - v
            hMap[compli] = i
        

            
        