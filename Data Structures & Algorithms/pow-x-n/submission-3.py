class Solution:
    def myPow(self, x: float, num: int) -> float:
        if num == 0:
            return 1
        n = abs(num)
        carry = 1
        while n > 1:
            if n%2 == 1:
                carry *= x
            x *= x
            n = n // 2         
        x *= carry
        return x if num > 0 else 1/x 