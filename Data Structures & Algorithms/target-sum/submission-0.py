class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        h = {}
        def dfs(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in h:
                return h[(i,total)]
            h[(i,total)] = dfs(i+1,total + nums[i]) + dfs(i+1,total - nums[i])
            return h[(i,total)]
            
        return dfs(0,0)
        