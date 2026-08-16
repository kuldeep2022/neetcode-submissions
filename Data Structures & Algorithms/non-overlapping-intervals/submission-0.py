class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        preEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= preEnd:
                preEnd = end
            else:
                res +=1
                preEnd = min(end,preEnd)
        
        return res

        