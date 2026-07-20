class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            total += n%2
            n = n >> 1
        return total