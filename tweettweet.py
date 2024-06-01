import tweepy # This is twitter api lib
import time

# These are the keys to access X api
auth = tweepy.OAuthHandler("SNBErH0UETpKqFcOWZbzQtUYU", "egWgU1TK7tSjtXqstLZ10yhwvhwe7bxwMviJs8lFWDMng4wtq6") # consumer API keys
auth.set_access_token("1606081593541533697-rs4doHu9EgKKmVVa5ek57LMnHcYPkJ", "R5Cvy7rSRyy1YMtxyK7aeL7b99h14y7uzZpprdgaVsEb3") # Access Token

# This authorized access to X api
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break