class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        res = []
        for i in queries:
            r = float("inf")
            for inter in intervals:
                if inter[0] > i:
                    break
                elif inter[1] >= i:
                    r = min(r,inter[1]-inter[0]+1)
            if r == float("inf"):
                r=-1
            res.append(r)

        return res