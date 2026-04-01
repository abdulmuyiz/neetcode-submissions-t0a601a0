class Solution:
    def isValid(self, s: str) -> bool:
        o = ['(','{','[']
        result = []
        if(len(s)%2 != 0):
            return False
        for i in s:
            if i in o:
                result.append(i)
            else:
                if (len(result)==0):
                    return False
                if (i==')' and result[-1] == '(') or (i=='}' and result[-1] == '{') or (i==']' and result[-1] == '[') :
                    result.pop()
                else:
                    return False
        if(len(result)==0):
            return True
        else:
            return False
