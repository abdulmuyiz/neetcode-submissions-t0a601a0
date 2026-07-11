class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []
        candidates = sorted(candidates)

        def func(i,sub,total):
            if total == target:
                res.append(sub.copy())
                return

            if i>=len(candidates) or total > target:
                return

            sub.append(candidates[i])
            func(i+1,sub,total + candidates[i])
            check = sub.pop()
            while i < len(candidates) and check == candidates[i]:
                i = i + 1    
            func(i,sub,total)

        func(0,[],0)
        # result = []
        # for i in res:
        #     result.append(list(i))

        return res