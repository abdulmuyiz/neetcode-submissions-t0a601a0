class Solution:
    def reverseBits(self, n: int) -> int:
        ans = n % 2
        for i in range(30,-1,-1):
            ans = ans << 1
            n = n >> 1
            ans = ans + n % 2  
        return ans