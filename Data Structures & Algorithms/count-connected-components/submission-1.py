class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}
        res = 0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):
            if i in visit:
                return

            visit.add(i)
            for nxt in adj[i]:
                dfs(nxt)

        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)

        return res

            