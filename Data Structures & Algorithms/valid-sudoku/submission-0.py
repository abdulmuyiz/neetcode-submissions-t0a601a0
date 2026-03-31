class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            for j in range(0,9):
                if(board[i][j] != "."):
                    for k in range(i+1,9):
                        if(board[i][j] == board[k][j]):
                            return False
                    for l in range(j+1,9):
                        if(board[i][j] == board[i][l]):
                            return False
                    row_start = (i // 3) * 3
                    col_start = (j // 3) * 3
                    for r in range(row_start, row_start + 3):
                        for c in range(col_start, col_start + 3):
                            if(board[i][j] == board[r][c] and i!=r and j!=c):
                                return False
        return True