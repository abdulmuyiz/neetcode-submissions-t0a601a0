class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        res = []

        def perm(sub,nums):
            if not nums:
                res.append(sub.copy())
                return

            for i in range(len(nums)):
                sub.append(nums[i])
                perm(sub,nums[:i]+nums[i+1:])
                sub.remove(nums[i])
        
        perm([],nums)
        return res