class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            ans = ans + n % 2
            ans = ans << 1 
            n = n >> 1 
        return ans >> 1