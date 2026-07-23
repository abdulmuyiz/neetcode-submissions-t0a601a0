class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bot = 0, len(matrix)
        r, l = 0, len(matrix[0])
        res = []
        total = l * bot
        while True :
            for i in range(r,l):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bot):
                res.append(matrix[i][l-1])
            l -= 1
            if top >= bot or r >= l:
                break
            for i in range(l-1,r-1,-1):
                res.append(matrix[bot-1][i])
            bot -= 1
            for i in range(bot-1,top-1,-1):
                res.append(matrix[i][r])
            r += 1
            if top >= bot or r >= l:
                break
        return res