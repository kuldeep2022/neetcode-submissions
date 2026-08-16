"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        p1,p2 =0,0
        res = 0
        while p1 < len(intervals):
            if start[p1]>= end[p2]:
                res-=1
                p2+=1
            res+=1
            p1+=1
            
        return res
            

        