class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visit = {}

        def dfs(prev, i,j):
            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]) or prev >= matrix[i][j]:
                return 0
            if (i,j) in visit:
                return visit[(i,j)]
            
            visit[(i,j)] = 1
            visit[(i,j)] += max(dfs(matrix[i][j],i+1,j),dfs(matrix[i][j],i,j+1),dfs(matrix[i][j],i-1,j),dfs(matrix[i][j],i,j-1))

            return visit[(i,j)]
        
        m = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m,dfs(-1,i,j))
        return m