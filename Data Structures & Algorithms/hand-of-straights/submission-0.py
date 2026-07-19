class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize == 1:
            return False
        hand.sort()
        prev = [[-1,0] for i in range(len(hand) // groupSize)]
        l = []
        for i in range(len(hand)):
            check = False
            print(prev)
            for j in range(len(prev)):
                if (prev[j][0] == -1 or (hand[i]-prev[j][0]) == 1) and prev[j][1] < groupSize:
                    prev[j][0] = hand[i]
                    prev[j][1] += 1
                    check = True
                    break
            if not check:
                return check
        return True