class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # followerId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []

        # 自己的 tweets
        all_tweets.extend(self.tweets[userId])

        # follow 的人的 tweets
        for followeeId in self.following[userId]:
            all_tweets.extend(self.tweets[followeeId])

        # 按时间从新到旧排序
        all_tweets.sort(reverse=True)

        return [tweetId for time, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)