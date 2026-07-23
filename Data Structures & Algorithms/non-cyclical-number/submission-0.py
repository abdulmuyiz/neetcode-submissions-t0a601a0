class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            temp = 0
            while n:
                dig = n%10
                n = n // 10
                temp += dig**2
            n = temp

        return True if n == 1 else False