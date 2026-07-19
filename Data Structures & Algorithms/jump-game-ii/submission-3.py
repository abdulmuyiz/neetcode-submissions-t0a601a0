class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jump = 0
        while i < len(nums)-1 and nums[i] != 0:
            m = -1
            for ind in range(i+1,i+nums[i]+1):
                print(ind,m)
                if ind == len(nums)-1:
                    return(jump+1)
                if m <= nums[ind] or ind + nums[ind] > m:
                    m = nums[ind]
                    i = ind
            jump += 1
        return jump