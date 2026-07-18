class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        j = i+1
        res =[]
        while j < len(intervals):
            if intervals[i][1] < intervals[j][0]:
                res.append(intervals[i])
                i = j
            else:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
            j += 1

        res.append(intervals[i])
        print(intervals)
        return res