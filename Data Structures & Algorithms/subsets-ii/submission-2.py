class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()

            #skip duplicates
            while i< len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,subset)
        
        nums.sort()

        dfs(0,[])
        return res