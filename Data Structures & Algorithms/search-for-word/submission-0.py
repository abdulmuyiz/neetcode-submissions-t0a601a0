class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.res = False

        def dfs(i,j,visit,l,s: str):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or l >= len(word) or word[l] != board[i][j] or (i,j) in visit:
                return

            visit.add((i,j))
            s += word[l]
            
            if word == s:
                self.res =  True
                return

            dfs(i+1,j,visit,l+1,s) 
            dfs(i,j+1,visit,l+1,s)
            dfs(i-1,j,visit,l+1,s)
            dfs(i,j-1,visit,l+1,s)

            s = s[:-1]
            visit.remove((i,j))
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,set(),0,"")

        
        return self.res