class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero = 0
        for i in nums:
            if i != 0:
                p *= i
            else:
                zero += 1
        
        for i in range(0,len(nums)):
            if nums[i] != 0 and zero == 0:
                nums[i] = int(p/nums[i])
            elif nums[i] != 0 and zero > 0:
                nums[i] = 0
            elif nums[i] == 0 and zero > 1:
                nums[i] = 0
            else:
                nums[i] = p
        
        return nums