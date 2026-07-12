class Twitter:

    def __init__(self):
        self.recent = 0
        self.userId = 0
        self.followlist = dict(set())
        self.tweet = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userId = userId
        self.recent += 1
        if userId in self.tweet:
            self.tweet[userId].append([self.recent,tweetId])
        else:
            self.tweet[userId] = [[self.recent,tweetId]]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        feed = [] if userId not in self.tweet else self.tweet[userId].copy()
        if userId in self.followlist:
            for i in self.followlist[userId]:
                if i in self.tweet and userId != i:
                    feed += self.tweet[i].copy()

        heapq.heapify_max(feed)
        print(feed)
        count = 10
        while feed and count:
            count -= 1
            res.append(heapq.heappop_max(feed)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followlist:
            self.followlist[followerId] = set()
        self.followlist[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followeeId in self.followlist[followerId]:
            self.followlist[followerId].remove(followeeId)
