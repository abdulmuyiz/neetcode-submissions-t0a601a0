class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]==0:
                return 0

            grid[i][j]=0
            return (1+dfs(i,j+1)+dfs(i+1,j)+dfs(i,j-1)+dfs(i-1,j))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area,dfs(i,j))

        return area