class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        res = 0
        check = False
        if x < 0:
            x *= -1
            check = True
        while x != 0:
            digit = x % 10 
            x = x//10
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res*10) + digit
            
        return res * -1 if check else res