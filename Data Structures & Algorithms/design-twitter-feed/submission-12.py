class Twitter:

    def __init__(self):
        self.recent = 0
        self.followlist = {}
        self.tweet = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.recent += 1
        if userId in self.tweet:
            self.tweet[userId].append([self.recent,tweetId])
        else:
            self.tweet[userId] = [[self.recent,tweetId]]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        if userId not in self.followlist:
            self.followlist[userId] = set()
        self.followlist[userId].add(userId)
        if userId in self.followlist:
            for followeeId in self.followlist[userId]:
                if followeeId in self.tweet:
                    index = len(self.tweet[followeeId])-1
                    count , tweetId = self.tweet[followeeId][index]
                    heap.append([count , tweetId, followeeId, index-1])

        heapq.heapify_max(heap)
        while heap and len(res)<10:
            count , tweetId, followeeId, index = heapq.heappop_max(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet[followeeId][index]
                heapq.heappush_max(heap, [count , tweetId, followeeId, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followlist:
            self.followlist[followerId] = set()
        self.followlist[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followeeId in self.followlist[followerId]:
            self.followlist[followerId].remove(followeeId)
