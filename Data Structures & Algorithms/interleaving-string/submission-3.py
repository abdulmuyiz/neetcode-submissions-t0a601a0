class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        d = {}
        def dfs(i,j):
            if (i,j) in d:
                return d[(i,j)]
            if i+j == len(s3):
                return i == len(s1) and j == len(s2)
            d[(i,j)] = False
            if i < len(s1) and s1[i] == s3[i+j]:
                d[(i,j)] = d[(i,j)] or dfs(i+1,j)
            if j < len(s2) and s2[j] == s3[i+j]:
                d[(i,j)] = d[(i,j)] or dfs(i,j+1)

            return d[(i,j)]

        return dfs(0,0)