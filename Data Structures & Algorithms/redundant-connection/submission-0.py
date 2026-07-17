class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = {}
        cycle = set()

        val = []

        for start, end in edges:
            if not start in d:
                d[start] = []
            if not end in d:
                d[end] = []
            d[start].append(end)
            d[end].append(start)

        def dfs(prev,i):
            if i in cycle:
                val.append([prev,i])
                return
            cycle.add(i)
            for nxt in d[i]:
                if prev != nxt:
                    dfs(i,nxt)
            cycle.remove(i)

        print(d)
        for i in d.keys():
            dfs(-1,i)

        for i in range(len(edges)-1,-1,-1):
            if edges[i] in val:
                return edges[i]

