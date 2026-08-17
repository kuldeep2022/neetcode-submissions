class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self,nums,idx):
        if idx == len(nums):
            self.res.append(nums.copy())
            return 
        
        used = set()
        
        for i in range(idx,len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            nums[idx],nums[i] = nums[i],nums[idx]
            self.backtrack(nums,idx+1)
            nums[idx],nums[i] = nums[i],nums[idx]
        
        