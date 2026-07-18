"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x:x.start)
        prev = intervals[0].end
        for i in range(1,len(intervals)):
            if prev > intervals[i].start:
                return False
            else:
                prev = intervals[i].end

        return True