class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1 and nums[i] != 0:
            m = -1
            for ind in range(i+1,i+nums[i]+1):
                if ind == len(nums)-1:
                    return True
                if m <= nums[ind] or ind - i >= m:
                    m = nums[ind]
                    i = ind
        return True if len(nums) == 1 else False