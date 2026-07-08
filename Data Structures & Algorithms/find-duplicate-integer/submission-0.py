class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        s=0
        while True:
            s = nums[s]
            slow = nums[slow]
            if s == slow:
                return slow