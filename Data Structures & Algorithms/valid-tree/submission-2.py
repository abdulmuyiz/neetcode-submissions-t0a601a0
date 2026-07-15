class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        cycle = set()
        adj = {i : [] for i in range(n)}

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        def dfs(pre,i):
            print(i,pre)
            if i in cycle:
                return False
            if i in visit:
                return True

            cycle.add(i)
            for nxt in adj[i]:
                if pre != nxt:
                    if not dfs(i,nxt):
                        return False

            cycle.remove(i)
            visit.add(i)
            return True
    
        if not dfs(-1,0):
            return False
            
        return True if len(visit) == n else False