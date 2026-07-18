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
        ava = []
        for i in range(len(intervals)):
            if ava and intervals[i].start < ava[0]:
                res += 1
            if ava and intervals[i].start >= ava[0]:
                heapq.heappop(ava)
            heapq.heappush(ava,intervals[i].end)
        
        return res
        