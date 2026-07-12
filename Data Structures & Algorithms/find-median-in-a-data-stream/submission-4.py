class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.rightheap = []
        heapq.heapify(self.rightheap)

    def addNum(self, num: int) -> None:
        if not self.leftheap:
            heapq.heappush_max(self.leftheap,num)
            return

        if len(self.leftheap) > len(self.rightheap):
            if self.leftheap[0] > num:
                temp = heapq.heappop_max(self.leftheap)
                heapq.heappush_max(self.leftheap, num)
                heapq.heappush(self.rightheap,temp)
            else:
                heapq.heappush(self.rightheap,num)
        else:
            if self.rightheap[0] <= num:
                temp = heapq.heappop(self.rightheap)
                heapq.heappush(self.rightheap, num)
                heapq.heappush_max(self.leftheap,temp)
            else:
                heapq.heappush_max(self.leftheap,num)



    def findMedian(self) -> float:
        print(self.leftheap, self.rightheap)
        return float(self.leftheap[0]) if len(self.leftheap) > len(self.rightheap) else (self.leftheap[0] + self.rightheap[0]) / 2
        