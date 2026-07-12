class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        res = 0
        letter = ""
        m= 0
        for t in tasks:
            d[t] = d.get(t,0) + 1
            m = max(m,d[t])
            if m == d[t]:
                letter = t
        while d[letter] > 1:
            d[letter] -= 1
            res += 1
            check = 0
            for ch in d:
                if letter != ch and d[ch] > 0:
                    d[ch] -= 1
                    res += 1
                    check += 1
                if check == n:
                    break
            res += (n-check)
        print(d)        
        for ch in d:
            res += d[ch]

        return res