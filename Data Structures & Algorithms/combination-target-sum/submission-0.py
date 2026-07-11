class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        sub = []

        def rec(i):
            if i>= len(nums) or sum(sub) > target:
                return

            if sum(sub) == target:
                res.add(tuple(sub.copy()))
                return

            sub.append(nums[i])
            rec(i)
            rec(i+1)
            sub.pop()
            rec(i+1)

        rec(0)
        result = []
        for i in res:
            result.append(list(i))

        return result