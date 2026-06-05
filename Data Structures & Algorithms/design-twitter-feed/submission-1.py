class Tweet:
    def __init__(self,tweetId,time):
        self.tweetId = tweetId
        self.time = time

class User:
    def __init__(self,userId):
        self.userId=userId
        self.followed=set()
        self.follow(userId)
        self.tweets=[]
    
    def follow(self, followeeId):
        self.followed.add(followeeId)
    
    def unfollow(self,unfollowId):
        if unfollowId != self.userId:
            self.followed.discard(unfollowId)
    
    def post(self,tweetId,time):
        new_tweet=Tweet(tweetId,time)
        self.tweets.append(new_tweet)

class Twitter:

    def __init__(self):
        self.time=0
        self.users={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId]=User(userId)
        
        user=self.users[userId]
        user.post(tweetId,self.time)
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        res=[]
        heap=[]
        user=self.users[userId]
        
        for followee_id in user.followed:
            followee=self.users[followee_id]

            if not followee or not followee.tweets:
                continue
            
            tweet=followee.tweets[-1]
            index = len(followee.tweets)-1

            tweet_time=tweet.time
            tweet_id=tweet.tweetId
            heapq.heappush(heap,(-tweet_time,tweet_id,followee_id,index))

        while heap and len(res)<10:
            neg_tweet_time,tweet_id,followee_id,index=heapq.heappop(heap)
            res.append(tweet_id)
            prev_idx=index-1
            if prev_idx >= 0:
                prev_twt=self.users[followee_id].tweets[prev_idx]

                heapq.heappush(heap,(-prev_twt.time,prev_twt.tweetId,followee_id,prev_idx))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId]=User(followeeId)
        if followerId not in self.users:
            self.users[followerId]=User(followerId)
        
        follower=self.users[followerId]
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)
        
