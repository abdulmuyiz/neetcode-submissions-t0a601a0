class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        m = max(nums)
        total = 0
        while i < len(nums):
            total += nums[i]
            if total < 0:
                total = 0
            else:
                m = max(m,total)
            i+=1

        return m
