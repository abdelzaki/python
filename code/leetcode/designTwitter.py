from collections import defaultdict


import heapq
class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)  # key = userID, value = tweet, time
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        self.followerMap[userId].add(userId)
        maxHeap = list()
        tweetsList = list()
        for followee in self.followerMap[userId]:
            lastIndex = len(self.tweetsMap[followee]) - 1
            if lastIndex >= 0:
                time, tweetId = self.tweetsMap[followee][lastIndex]
                maxHeap.append((time, tweetId, lastIndex - 1, followee))
        heapq.heapify(maxHeap)
        while maxHeap and len(tweetsList) < 10:
            _time, tweetId, lastIndex, followee = heapq.heappop(maxHeap)
            if lastIndex >= 0:
                time, tweetId = self.tweetsMap[followee][lastIndex]
                heapq.heappush(maxHeap, (time, tweetId, lastIndex-1,followee))
            tweetsList.append(tweetId)

        return tweetsList       

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self,followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        """
        ["Twitter","","","","","",""]
            [[], postTweet[1,1],getNewsFeed[1],follow[2,1],getNewsFeed[2],unfollow[2,1],
            getNewsFeed[2]]

        """
obj = Twitter()
obj.postTweet(1,1)
param_2 = obj.getNewsFeed(1)
obj.follow(2,1)
param_2 = obj.getNewsFeed(2)
param_2 = obj.getNewsFeed(2)

