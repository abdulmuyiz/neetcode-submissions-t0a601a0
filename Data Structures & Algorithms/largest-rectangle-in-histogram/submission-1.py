class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area =0
        for i,h in enumerate(heights):
            ele = []
            while stack and stack[-1][1] > h:
                ele = stack.pop()
                max_area = max(max_area,ele[1] * (i-ele[0]))
            if ele:
                stack.append([ele[0],h])
            else:
                stack.append([i,h])

        while stack:
            ele = stack.pop()
            max_area = max(max_area , ele[1] * (len(heights)-ele[0]))

        return max_area
