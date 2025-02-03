#app id 30068637
import tweepy
import tweepy.client

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJ3PygEAAAAA57lg0jvD86yDM2Fj1K%2BTe%2BxnD2c%3DbBP84lTuIG4WbZ0xBJ7kc4dJfICDGm6cqAqUKyjQe70xxbarVp"



# Authenticate with Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Fetch recent tweets with a keyword
query = "machine learning -is:retweet lang:en"  # Exclude retweets
tweets = client.search_recent_tweets(query=query, max_results=10)

# Print tweets
for tweet in tweets.data:
    print(tweet.text)
