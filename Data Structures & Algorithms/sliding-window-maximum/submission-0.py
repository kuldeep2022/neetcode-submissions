class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # we will be maintaining monotonic decresing queue
        res = []
        l,r = 0,0

        while r < len(nums):
            # Our queue will contain indices
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                # Out of the window size
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l+=1
            
            r += 1
        return res

        