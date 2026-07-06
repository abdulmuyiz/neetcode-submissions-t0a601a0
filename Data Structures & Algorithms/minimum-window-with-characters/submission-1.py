class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) < len(t)): return ""
        
        pattern = {}
        for i in t:
            pattern[i] = 1 + pattern.get(i , 0)
        l = 0
        short = float("inf")
        index = [0,0]
        for r in range(len(s)):
            if s[r] in pattern:
                pattern[s[r]] -= 1
                
            while max(pattern.values()) <= 0:
                if short > r - l + 1:
                    short = r - l + 1
                    index = [l,r+1]
                if s[l] in pattern:
                    pattern[s[l]] += 1
                l += 1
                
        return  "" if short == float("inf") else s[index[0]:index[1]]
