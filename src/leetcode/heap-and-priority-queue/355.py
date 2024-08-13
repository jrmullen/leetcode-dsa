class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # Map follower ID to a hashset containing followee IDs
        self.tweetCount = 0 # Track the total number of tweets so they can retrieved in order
        self.tweets = defaultdict(list) # Map user ID to a heap containing tuples (tweetCount, tweet ID)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweetCount, tweetId))
        self.tweetCount -= 1 # Update the tweet count to account for the new tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        # Initialize a list to be heapified as a minHeap
        minHeap = []
        result = [] # The final list of tweetIds to be returned

        # The news feed includes the user's own tweets, so add the user as a follower of themself
        self.following[userId].add(userId)

        # Fetch all of the user's follower's most recent tweets and push them to `heap`
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1 # Snapshot the index of the user's most recent tweet
                countId, tweetId = self.tweets[followeeId][index]
                minHeap.append([countId, tweetId, followeeId, index - 1])
        
        # Heapify
        heapq.heapify(minHeap) # Heapifying `heap` will use the first element, `countId`, as the key

        # Push the tweets to the final `result` list until there are either no tweets remaining, or there are 10
        while minHeap and len(result) < 10:
            # Pop the most recent tweet and append it to the final `result` list
            countId, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)

            # Update the heap by fetching the next most recent tweet from user `followeeId` and push it onto the heap
            if index >= 0:
                countId, tweetId = self.tweets[followeeId][index] # Index contains a snapshot of the next tweet to fetch
                heapq.heappush(minHeap, [countId, tweetId, followeeId, index - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
