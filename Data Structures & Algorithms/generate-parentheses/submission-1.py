class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def recur(open,close,p):
            if open < 0 or close < 0:
                return

            if open == close == 0:
                res.append(p)
                return

            p += "("
            recur(open-1,close+1,p)
            p = p[:-1]
            p += ")"
            recur(open,close-1,p)
            p = p[:-1]

        recur(n,0,"")

        return res