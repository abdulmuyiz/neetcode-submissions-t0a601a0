class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        matrix = [["."] * n for i in range(n)]

        v = set()
        d = set()
        o = set()

        def Queen(index):
            if index == n:
                copy = ["".join(row) for row in matrix]
                res.append(copy)
                return

            for i in range(n):
                if i not in v and (index-i) not in d and (index+i) not in o:

                    v.add(i)
                    d.add(index - i)
                    o.add(index+i)
                    matrix[index][i] =  "Q"

                    Queen(index+1)

                    v.remove(i)
                    o.remove(index+i)
                    d.remove(index - i)
                    matrix[index][i]  = "."


        Queen(0)
        return res