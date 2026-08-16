"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True

        intervals.sort(key=lambda x:x.start)
        lastEndTime = float("-inf")

        for i,v in enumerate(intervals):
            #print("Start TIme", v.start, "Last End", lastEndTime)
            if v.start < lastEndTime:
                return False
            else:
                lastEndTime = max(v.end,lastEndTime)
        
        return True

