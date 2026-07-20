class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        check = False
        if x < 0:
            x *= -1
            check = True
        while x != 0:
            res *= 10
            if res > 2**31-1 or res < -2**31:
                return 0
            res += x%10
            x = x//10
        if check:
            res *= -1
        return res