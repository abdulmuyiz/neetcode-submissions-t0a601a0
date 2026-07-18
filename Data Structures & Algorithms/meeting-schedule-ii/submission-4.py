"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        res = 1
        prev = intervals[0].end
        ava = set()
        ava.add(prev)
        for i in range(1,len(intervals)):
            print(ava)
            if prev > intervals[i].start and intervals[i].start < min(ava):
                res += 1
            if intervals[i].start >= min(ava):
                ava.remove(min(ava))
            ava.add(intervals[i].end)
            prev = intervals[i].end
        
        return res
        