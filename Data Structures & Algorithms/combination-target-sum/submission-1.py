class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, a = [], []
        def dfs(i, currSum):
            
            if i == len(nums) or currSum > target:
                return
            
            if currSum == target:
                ans.append(a.copy())
                return
            
            # Decision
            # Include Current
            currSum += nums[i]
            a.append(nums[i])
            dfs(i, currSum)
            currSum -= nums[i]
            a.pop()

            # Does not include current
            dfs(i+1,currSum)
        
        dfs(0,0)
        return (ans)


        