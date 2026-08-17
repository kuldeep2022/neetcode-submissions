class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        lcs = 0
        for i in nums:
            if i-1 not in s:
                count = 0
                while i+count in s:
                    count+= 1
                lcs = max(lcs, count)
        
        return lcs


        