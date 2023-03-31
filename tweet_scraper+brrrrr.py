import tweepy
import csv
import yaml

# load the API credentials from the YAML file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# set up the authentication with Twitter API
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

# set up the API with rate limits
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# set up the search query for the hashtag
search_query = "#crypto"


# set up the CSV file to save the tweets and their details
csv_file = open("tweets.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Tweet ID", "Tweet Text", "Likes", "Retweets", "Quote Tweets"])

# extract the tweets and their details
tweets = tweepy.Cursor(api.search, q=search_query, lang="en", tweet_mode="extended").items(config["count"])
for tweet in tweets:
    if config.get("ignore_retweets") and hasattr(tweet, "retweeted_status"):
        continue
    tweet_id = tweet.id_str
    tweet_text = tweet.full_text
    tweet_likes = tweet.favorite_count
    tweet_retweets = tweet.retweet_count
    tweet_quotetweets = tweet.quote_count
    csv_writer.writerow([tweet_id, tweet_text, tweet_likes, tweet_retweets, tweet_quotetweets])

# close the CSV file
csv_file.close()
