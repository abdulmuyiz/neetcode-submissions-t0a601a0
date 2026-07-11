class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def func(i,sub):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            func(i+1,sub)
            n = sub.pop()
            while i < len(nums) and n == nums[i]:
                i = i+1
            func(i,sub)


        func(0,[])

        return res