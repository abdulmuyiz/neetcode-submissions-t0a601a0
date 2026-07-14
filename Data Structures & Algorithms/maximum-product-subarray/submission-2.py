class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0,0,0] for i in nums]
        dp[0] = [nums[0],nums[0],nums[0]]
        m = nums[0]
        for i in range(1,len(nums)):
            f = dp[i-1][0] * nums[i]
            s = dp[i-1][1] * nums[i]
            t = dp[i-1][2] * nums[i]
            dp[i][0] = max(f,s,t)
            dp[i][1] = min(f,s,t)
            dp[i][2] = nums[i]
            temp = max(dp[i])
            m = max(temp,m)

        return m