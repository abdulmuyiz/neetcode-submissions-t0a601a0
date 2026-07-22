class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        minH = [[grid[0][0],0,0]]
        x,y = 0,0 
        visit = set()
        while minH:
            water,x,y = heapq.heappop(minH)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            res = max(res,water)
            if  x == len(grid)-1 and y == len(grid[0])-1:
                break

            if x+1 < len(grid) and (x+1,y) not in visit:
                heapq.heappush(minH,[grid[x+1][y], x+1, y])
            if y+1 < len(grid[0]) and (x,y+1) not in visit:
                heapq.heappush(minH,[grid[x][y+1], x, y+1])
            if x-1 >= 0 and (x-1,y) not in visit:
                heapq.heappush(minH,[grid[x-1][y], x-1, y])
            if y-1 >= 0 and (x,y-1) not in visit:
                heapq.heappush(minH,[grid[x][y-1], x, y-1])

        return res

