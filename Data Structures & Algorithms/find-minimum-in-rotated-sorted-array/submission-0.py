class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        m = float("inf")
        while l <= h:
            mid = (h+l) // 2
            if  nums[mid] > nums[h]:
                l = mid + 1
            else:
                m = min(m, nums[mid])
                h = mid - 1
        return m
