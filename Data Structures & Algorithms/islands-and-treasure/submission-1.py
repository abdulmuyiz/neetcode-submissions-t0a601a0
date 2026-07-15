class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        def dfs(nums , i ,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or nums > grid[i][j]:
                return 

            grid[i][j] = nums
            dfs(nums+1,i+1,j)
            dfs(nums+1,i,j+1)
            dfs(nums+1,i-1,j)
            dfs(nums+1,i,j-1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(0,i,j)

        return