class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nextDp = set()
            for t in dp:
                nextDp.add(t+nums[i])
                nextDp.add(t)
            dp = nextDp
            if target in dp:
                return True


        return False