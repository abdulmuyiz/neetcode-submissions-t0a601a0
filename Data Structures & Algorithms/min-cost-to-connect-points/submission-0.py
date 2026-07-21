class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minH = [[0,0]]

        while len(visit) < N:
            cost, node = heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            res += cost
            for p in adj[node]:
                if p[1] not in visit:
                    heapq.heappush(minH,p)

        return res
