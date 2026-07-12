class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        while len(stones) > 1:
            heapq.heapify_max(stones)
            s1=heapq.heappop(stones)
            heapq.heapify_max(stones)
            s2=heapq.heappop(stones)
            if s1 == s2:
                continue
                
            print(s1,s2) 
            heapq.heappush(stones,abs(s1-s2))

        return 0 if not stones else stones[0]