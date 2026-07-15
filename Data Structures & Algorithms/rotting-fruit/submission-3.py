class Solution:
	def orangesRotting(self,grid) -> int:
		q = deque()
		visit = set()

		def layer(i,j):
			if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or grid[i][j] == 2 or (i,j) in visit:
				return

			grid[i][j] = -1
			visit.add((i,j))
			q.append([i,j])
		
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 2:
					q.append([i,j])
		if not q:
			return 0 if  max(max(row) for row in grid) == 0 else -1

		time = 0
		while q:
			time += 1
			for i in range(len(q)):
				row,col = q.popleft()
				grid[row][col] = 0
				layer(row+1,col)
				layer(row,col+1)
				layer(row-1,col)
				layer(row,col-1)

		return (time-1) if  max(max(row) for row in grid) == 0 else -1
