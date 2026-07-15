class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visit = set()
        res = []
        check = [[[False,False] for _ in range(len(heights[0]))] for _ in range(len(heights))]

        def dfs(i,j):
            if i < 0 or j < 0:
                return [True,False]
            
            if i == len(heights) or j == len(heights[0]):
                return [False,True]

            if (i,j) in visit:
                return check[i][j]

            visit.add((i,j))
            if i-1 < 0 or heights[i][j] >= heights[i-1][j]:
                temp = dfs(i-1,j)
                check[i][j][0] = check[i][j][0] or temp[0]
                check[i][j][1] = check[i][j][1] or temp[1]

            if check[i][j][1] and check[i][j][0]:
                return check[i][j]

            if j-1 < 0 or heights[i][j] >= heights[i][j-1]:
                temp = dfs(i,j-1) 
                check[i][j][0] = check[i][j][0] or temp[0]
                check[i][j][1] = check[i][j][1] or temp[1]

            if check[i][j][1] and check[i][j][0]:
                return check[i][j]
            
            if j+1 == len(heights[0]) or heights[i][j] >= heights[i][j+1]:
                temp = dfs(i,j+1)
                check[i][j][0] = check[i][j][0] or temp[0]
                check[i][j][1] = check[i][j][1] or temp[1]

            if check[i][j][1] and check[i][j][0]:
                return check[i][j]

            if i+1 == len(heights) or heights[i][j] >= heights[i+1][j]:
                temp = dfs(i+1,j)
                check[i][j][0] = check[i][j][0] or temp[0]
                check[i][j][1] = check[i][j][1] or temp[1]

            return check[i][j]


        for i in range(len(heights)):
            for j in range(len(heights[0])):
                p , a = dfs(i,j)
                if p and a:
                    res.append([i,j])
        print(check)

        return res