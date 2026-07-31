class Twitter:

    def __init__(self):
        self.UserFeed = defaultdict(list)
        self.timer = 0
        self.connection = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.UserFeed[userId], (self.timer, tweetId))
        self.timer += 1
        while len(self.UserFeed[userId]) > 10:
            heapq.heappop(self.UserFeed[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        result = self.UserFeed[userId][:]
        for following in self.connection[userId]:
            for feed in self.UserFeed[following]:
                heapq.heappush(result, feed)
        return [feed[1] for feed in sorted(result, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.connection[followerId]:
            self.connection[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.connection[followerId]:
            self.connection[followerId].remove(followeeId)
