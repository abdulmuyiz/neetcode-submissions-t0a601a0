class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            if n % 2:
                ans += 2 ** i
                print (ans)
            n = n >> 1 

        return ans