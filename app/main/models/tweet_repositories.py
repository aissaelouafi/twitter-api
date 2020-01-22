from .tweet import Tweet
class TweetRepositories:
    def __init__(self):
        self.tweet_list = []
        pass

    def add(self, tweet):
        tweet.id = len(self.tweet_list)+1
        self.tweet_list.append(tweet)
        ## add a tweet id later

    def get(self, tweet_id):
        for tweet in self.tweet_list:
            if tweet.id == tweet_id:
                return tweet
        return None

    def clear(self):
        self.tweet_list = []




