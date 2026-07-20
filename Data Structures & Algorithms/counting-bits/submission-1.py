class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1,n+1):
            res.append((i%2) + res[i>>1])
        return res