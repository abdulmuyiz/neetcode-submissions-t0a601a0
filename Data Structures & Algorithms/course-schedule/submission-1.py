class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = [False] * numCourses
        course = {}
        visit = set()

        for i in prerequisites:
            if i[0] not in course:
                course[i[0]] = []
            course[i[0]].append(i[1])

        
        for i in range(numCourses):
            if i not in course:
                res[i] = True

        def dfs(i):
            if i in visit or i not in course:
                return res[i]

            visit.add(i)
            l = []
            for nxt in course[i]:
                l.append(dfs(nxt))
            res[i] = all(l)
            return res[i]
        
        for i in range(numCourses):
            if res[i] == False:
                dfs(i)

        
        return all(res)