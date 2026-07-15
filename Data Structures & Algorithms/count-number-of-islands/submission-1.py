class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        islands = 0
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == "0":
                return 0
            visited[i][j] = True

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

            return 1
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                islands += dfs(i,j)



        return islands