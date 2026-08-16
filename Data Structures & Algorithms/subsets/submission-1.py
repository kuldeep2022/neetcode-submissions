class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,container = [],[]

        def backtrack(i):
            if i == len(nums):
                res.append(container.copy())
                return
            
            #Option 1 - Does not include the current element
            backtrack(i+1)

            # Option 2 - Include the current element
            container.append(nums[i])
            backtrack(i+1)
            container.pop()
        
        backtrack(0)
        return res