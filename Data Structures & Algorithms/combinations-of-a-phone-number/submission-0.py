class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {"2" : "abc", "3": "def", "4":"ghi", "5": "jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        res = []
        word = []

        def dfs(index):
            if index == len(digits):
                res.append("".join(word))
                return

            for i in d[digits[index]]:
                word.append(i)
                dfs(index+1)
                word.pop()



        dfs(0)
        return res