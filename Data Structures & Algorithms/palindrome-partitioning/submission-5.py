class Solution:

    def check(self,s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i,j,l):

            if j > len(s) and "".join(l) == s:
                res.append(l.copy())
                return
            if j > len(s):
                return
            if self.check(s[i:j]):
                l.append(s[i:j])
                dfs(j,j+1,l)
                l.pop()
            # dfs(j,j+1,l)
            dfs(i,j+1,l)

        dfs(0,1,[])

        return res