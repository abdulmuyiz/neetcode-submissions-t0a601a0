class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        m = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                m = max(m,p-buy)

        return m