class Solution:
    def checkValidString(self, st: str) -> bool:
        s = []
        star = []
        for ind,i in enumerate(st):
            print(s,star)
            if i == "*":
                star.append(ind)
            elif i == "(":
                s.append(ind)
            elif i == ")":
                if not s and not star:
                    return False
                if s:
                    s.pop()
                else:
                    star.pop()

        while s and star:
            if s.pop() > star.pop():
                return False

        return not s