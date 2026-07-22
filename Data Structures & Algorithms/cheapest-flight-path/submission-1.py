class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visit = set()
        adj = { i : [] for i in range(n)}

        for start,end,cost in flights:
            adj[start].append([cost,end])

        minH = [[0,src,k]]

        while minH:
            print(minH)
            cost, node, lay = heapq.heappop(minH)
            if node == dst and lay >= -1:
                return cost
            if node in visit and lay < 0:
                continue
            visit.add(node)
            
            for nxt in adj[node]:
                heapq.heappush(minH,[cost+nxt[0],nxt[1],lay-1])

        return -1
