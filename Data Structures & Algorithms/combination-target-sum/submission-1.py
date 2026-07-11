class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(i,sub,total):
            if i>= len(nums) or total > target:
                return

            if total == target:
                res.append(sub.copy())
                return

            sub.append(nums[i])
            rec(i,sub,total+nums[i])
            sub.pop()
            rec(i+1,sub,total)

        rec(0,[],0)

        return res