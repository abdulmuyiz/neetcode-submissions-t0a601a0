class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [i for i in range(len(temperatures))]
        for i,t in enumerate(temperatures):
            if stack:
                while stack[-1][1] < t:
                    r = stack.pop()
                    output[r[0]] = i - r[0] 
                    if not stack:
                        break
            if not stack or stack[-1][1] >= t :
                stack.append([i,t])
            
        while len(stack) > 0:
            r = stack.pop()
            output[r[0]] =  0
        return output