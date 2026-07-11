class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        matrix = ["." *n ]*n

        v = set()
        d = set()
        o = set()

        def Queen(index):
            if index == n:
                res.append(matrix.copy())
                return

            for i in range(n):
                if i not in v and (index-i) not in d and (index+i) not in o:
                    char_list = list(matrix[index])

                    v.add(i)
                    d.add(index - i)
                    o.add(index+i)
                    char_list[i] = "Q"
                    matrix[index] =  "".join(char_list)

                    Queen(index+1)

                    v.remove(i)
                    o.remove(index+i)
                    d.remove(index - i)
                    char_list[i] = "."
                    matrix[index]= "".join(char_list)


        Queen(0)
        return res