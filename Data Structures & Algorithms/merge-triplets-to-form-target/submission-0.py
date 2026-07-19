class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []
        for first,sec,third in triplets:
            if first <= target[0] and sec <= target[1] and third <= target[2]:
                res.append([first,sec,third])
        
        check = [False,False,False]

        for first,sec,third in res:
            if first == target[0]:
                check[0] = True
            if sec == target[1]:
                check[1] = True
            if third == target[2]:
                check[2] = True

        return all(check)
