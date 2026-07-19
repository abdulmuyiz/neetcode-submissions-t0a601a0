class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        j = 0
        print(intervals,queries)
        for i in sorted(queries):
            while j < len(intervals):
                if intervals[j][0] > i:
                    break
                elif intervals[j][1] >= i:
                    heapq.heappush(minHeap,[intervals[j][1]-intervals[j][0]+1,intervals[j][1]])
                j += 1
            while minHeap and minHeap[0][1] < i:
                heapq.heappop(minHeap)
            res[i] = minHeap[0][0] if minHeap else -1

        ans = []
        for i in queries:
            ans.append(res[i])
            
        return ans