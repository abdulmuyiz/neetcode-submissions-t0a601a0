class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        fresh, minutes = 0, 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fresh >0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] !=1 or (row,col) in visit:
                        continue
                    grid[row][col] =2
                    q.append([row,col])
                    fresh-=1
            minutes+=1
        return minutes if fresh == 0 else -1