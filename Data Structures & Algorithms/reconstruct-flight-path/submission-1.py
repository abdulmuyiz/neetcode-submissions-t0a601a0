class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = {}
        tickets.sort()
        for start,end in tickets:
            if start not in path:
                path[start] = []
            path[start].append(end)

        res = ["JFK"]
        visit = set()
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in path:
                return False

            temp = list(path[node])
            for i, nxt in enumerate(temp):
                path[node].pop(i)
                res.append(nxt)

                if dfs(nxt): return True

                path[node].insert(i,nxt)
                res.pop()
            
            return False

        dfs("JFK")
        
        return res