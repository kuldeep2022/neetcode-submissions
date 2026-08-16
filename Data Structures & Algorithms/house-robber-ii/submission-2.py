class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(nums):
            h1 = h2 = 0
            for n in nums:
                t = max(h1+n,h2)
                h1 = h2
                h2 = t
            return h2
        return max(nums[0], helper(nums[1:]), helper(nums[:n-1]))
        