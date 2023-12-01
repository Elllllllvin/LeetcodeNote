> Problem: [355. 设计推特](https://leetcode.cn/problems/design-twitter/description/)

[toc]

# 思路

> 面向对象程序设计

# Code

```Python


class Twitter:


    def __init__(self):

        self.following = {}

        self.alltweets = []


    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.following:

            self.following[userId] = []


        self.alltweets.append([userId,tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.following.keys():

            return []

        else:

            ids = [userId]+self.following.get(userId) #待排查的users

            tmp = []

            count = 10

            for tweet in self.alltweets[-1:-(len(self.alltweets) + 1) : -1]:

                if count>0 and tweet[0] in ids:

                    tmp.append(tweet[1])

                    count -= 1

            return tmp


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:

            self.following[followerId] = []

        self.following[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following or followeeId not in self.following[followerId]:

            return

        else:        

            self.following[followerId].remove(followeeId)








# Your Twitter object will be instantiated and called as such:

# obj = Twitter()

# obj.postTweet(userId,tweetId)

# param_2 = obj.getNewsFeed(userId)

# obj.follow(followerId,followeeId)

# obj.unfollow(followerId,followeeId)

```
