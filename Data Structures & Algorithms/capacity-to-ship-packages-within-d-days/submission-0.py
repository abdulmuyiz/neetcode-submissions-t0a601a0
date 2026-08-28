class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        up = sum(weights)
        res = up

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap -w <0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while low <= up:
            cap = (low + up) // 2

            if canShip(cap):
                res = min(res,cap)
                up = cap - 1
            else:
                low = cap + 1

        return res