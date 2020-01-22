# tests/test_models.py
from unittest import TestCase
from app.main.models.tweet import Tweet  # We will code our `Tweet` class in `app/models.py`
from app.main.models.tweet_repositories import TweetRepositories

class TestTweetRepositories(TestCase):
    def test_empty_list(self):
        tweet_repositories = TweetRepositories()
        self.assertEqual(len(tweet_repositories.tweet_list), 0)

    def test_add_tweet(self):
        tweet_repositories = TweetRepositories()
        tweet = Tweet("first tweet")
        tweet_repositories.add(tweet)
        self.assertEqual(len(tweet_repositories.tweet_list), 1)

    def test_get_id(self):
        tweet_repositories = TweetRepositories()
        tweet = Tweet("first tweet")
        tweet_repositories.add(tweet)
        tweet_2 = Tweet("second tweet")
        tweet_repositories.add(tweet_2)
        self.assertEqual(tweet.id, 1)
        self.assertEqual(tweet_2.id, 2)


    def test_get_id(self):
        tweet_repositories = TweetRepositories()
        tweet = Tweet("first tweet")
        tweet_repositories.add(tweet)
        tweet_by_id = tweet_repositories.get(1)
        self.assertEqual(tweet_by_id.text , "first tweet")


