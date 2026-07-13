class Solution:
    def numDecodings(self, s: str) -> int:
        d = {str(i): chr(96 + i) for i in range(1, 27)} 
        dp = [0] * len(s)

        dp[0] = 1
        if s[0] not in d:
            return 0

        if len(s) == 1:
            return 1

        dp[1] = (1 if s[1] in d else 0) + (1 if s[:2] in d else 0)
        
        for i in range(2,len(s)):
            if s[i] not in d and s[i-1:i+1] not in d:
                return 0 

            if s[i] in d and s[i-1:i+1] not in d:
                dp[i] = dp[i-1]
            elif s[i] not in d and s[i-1:i+1] in d:
                dp[i-1] = dp[i-2]
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2]

            print(dp)


        return dp[len(s)-1]
            


