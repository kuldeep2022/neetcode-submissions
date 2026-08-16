class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ans = float('inf')
        while l<=r:
            mid = (r+l)//2
            ans = min(ans,nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return ans

        