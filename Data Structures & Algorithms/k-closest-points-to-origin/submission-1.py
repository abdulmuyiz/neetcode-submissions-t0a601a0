class Solution:

    # def heapify(self,d)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in points:
            i.insert(0,i[0] * i[0] + i[1] * i[1])

        heapq.heapify(points)
        print(points)
        while len(res) < k:
            p = heapq.heappop(points)
            res.append([p[1],p[2]]) 

        return res