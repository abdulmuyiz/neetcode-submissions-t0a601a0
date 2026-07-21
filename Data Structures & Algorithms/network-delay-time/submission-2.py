class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        adj = {}
        for n1,n2,time in times:
            if n1 not in adj:
                adj[n1] = []
            adj[n1].append([n2,time])
        
        q = [[0,k]]
        t = 0
        while q:
            path,node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            t = max(path,t)
            if node in adj:
                for nxt,travel in adj[node]:
                    if nxt not in visit:
                        heapq.heappush(q,[path+travel,nxt])
            

        return t if len(visit) == n else -1

