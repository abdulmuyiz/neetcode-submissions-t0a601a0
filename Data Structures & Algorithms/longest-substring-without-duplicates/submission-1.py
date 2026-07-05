class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,max_len = 0,0,0
        characters = set()
        while r < len(s):
            while(s[r] in characters):
                characters.remove(s[l])
                l += 1    
            characters.add(s[r])
            r += 1       
            max_len = max(max_len , r - l)

        return max_len
