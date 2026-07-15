class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        cycle = set()
        adj = {i : [] for i in range(n)}

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        def dfs(pre,i):
            if i in visit:
                return False

            visit.add(i)
            for nxt in adj[i]:
                if pre != nxt:
                    if not dfs(i,nxt):
                        return False

            
            return True
            
        return dfs(-1,0) and len(visit) == n