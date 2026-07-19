class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        m = 0
        res = -1
        for i in range(len(gas)):
            m += gas[i] - cost[i]
            if m < 0:
                m = 0
                res = i
        return res+1