class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [False] * numCourses
        course = {i: [] for i in range(numCourses)}
        visit = set()
        ans = []

        for i in prerequisites:
            course[i[0]].append(i[1])
      
        for i in range(numCourses):
            if i not in course:
                res[i] = True
                ans.append(i)

        def dfs(i):
            if i in visit or i not in course:
                return res[i]
            visit.add(i)
            l = []
            for nxt in course[i]:
                l.append(dfs(nxt))
            res[i] = all(l)
            if res[i]:
                ans.append(i)
            return res[i]
        
        for i in range(numCourses):
            if res[i] == False:
                dfs(i)       
        return [] if not all(res) else ans