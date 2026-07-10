class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res= []
        l = []

        def func(i):
            if i >= len(nums):
                res.append(l.copy())
                return

            l.append(nums[i])
            func(i + 1)
            l.pop()
            func(i + 1)

        func(0)
        return res