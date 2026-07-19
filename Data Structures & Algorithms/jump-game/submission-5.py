class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                return False
            m = -1
            count = 0
            for ind in range(i+1,i+nums[i]+1):
                count += 1
                if ind == len(nums)-1:
                    return True
                if m <= nums[ind] or count >= m:
                    count = 0
                    m = nums[ind]
                    i = ind
        return True if len(nums) == 1 else False