class Solution:
    def trap(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area = 0
        maxl = heights[l]
        maxr = heights[r]
        while (l<r):
            if (maxl<maxr):
                l+=1
                maxl = max(maxl, heights[l])
                area += maxl - heights[l]
            else:
                r-=1
                maxr = max(maxr, heights[r])
                area += maxr - heights[r]
        return area

            