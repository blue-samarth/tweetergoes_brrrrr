import openai
import pandas as pd

# Set up OpenAI API
openai.api_key = "<YOUR API KEY>"

# Read CSV file with tweet data
tweets_df = pd.read_csv("tweets.csv")

# Concatenate all tweet descriptions
tweet_desc = " ".join(tweets_df["tweet_desc"].tolist())

# Use OpenAI to summarize the tweet descriptions
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=(f"Please summarize the following tweets: \n{tweet_desc}"),
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Extract the summarized news story from OpenAI's response
news_story = response.choices[0].text.strip()

print(news_story)
