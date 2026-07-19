class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        char = set()
        d = Counter(s)
        res = []
        sub = 0
        
        for i in range(len(s)):
            char.add(s[i])
            sub += 1
            d[s[i]] -= 1
            if d[s[i]] == 0:
                char.remove(s[i])
            if not char:
                res.append(sub)
                sub = 0

        return res
                
