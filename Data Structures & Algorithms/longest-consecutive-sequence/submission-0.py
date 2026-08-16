class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for i in nums:
            if i-1 not in s:
                longest = 0
                while i+longest in s:
                    longest +=1
                maxLen = max(maxLen,longest)
                
 
        return maxLen
        