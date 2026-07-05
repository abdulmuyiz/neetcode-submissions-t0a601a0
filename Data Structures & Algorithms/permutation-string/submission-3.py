class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)

        res, l =0,0

        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
            if r-l > len(s1)-1:
                if s2[l] in count:
                    count[s2[l]] += 1
                l += 1 
            if max(count.values()) == 0 :
                return True

        return False