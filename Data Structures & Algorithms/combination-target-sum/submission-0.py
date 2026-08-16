class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            # Base cases
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # 1st choice to include the candidate so
            cur.append(nums[i])
            dfs(i,cur,total + nums[i])

            # 2nd choice is not to include the candidate so
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0,[],0)
        return res

        