class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]

        for i in range(1,m):
            newDp = [1] * n
            for j in range(1,n):
                newDp[j] = newDp[j-1]+dp[j]
            dp = newDp
        return dp[n-1]