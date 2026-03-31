class Solution:
    def isPalindrome(self, s: str) -> bool:
        main = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        t = [char for char in s if char in main]
        return t == t[::-1]