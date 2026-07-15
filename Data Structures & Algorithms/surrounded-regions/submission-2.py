class Solution:
    def solve(self, board: List[List[str]]) -> None:
        check = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        visit = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] == "X" or (i,j) in visit:
                return 

            check[i][j] = True
            visit.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)

        for j in range(len(board[0])):
            dfs(0,j)
            dfs(len(board)-1,j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if check[i][j] == False:
                    board[i][j] = "X"