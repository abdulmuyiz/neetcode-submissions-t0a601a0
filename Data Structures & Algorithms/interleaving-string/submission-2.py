class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        d = {}
        def dfs(i,j,new):
            if (i,j) in d:
                return d[(i,j)]
            if new == len(s3) and i == len(s1) and j == len(s2):
                return True
            if new == len(s3) or ( i == len(s1) and j == len(s2) ):
                return False
            d[(i,j)] = False
            if i < len(s1) and s1[i] == s3[new]:
                d[(i,j)] = d[(i,j)] or dfs(i+1,j,new+1)
            if j < len(s2) and s2[j] == s3[new]:
                d[(i,j)] = d[(i,j)] or dfs(i,j+1,new+1)

            return d[(i,j)]

        return dfs(0,0,0)