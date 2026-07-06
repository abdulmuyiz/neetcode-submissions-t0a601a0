class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l+r)//2
            eat = 0
            for banana in piles:
                eat += banana//mid if banana%mid == 0 else (banana//mid) + 1
            if eat <= h:
                r = mid - 1
                res = min(res,mid)
            else:
                l = mid + 1

        return res
