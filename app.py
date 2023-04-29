from tweety.bot import Twitter
from pydantic import BaseModel, Field
import pandas as pd
from workcell.integrations.types import PerspectiveTable


class Input(BaseModel):
    username: str = Field(default="sama", description="Twitter username of the person you want to scrape")

def fetch_twitter_by_id(username):
    # app = Twitter("elonmusk")
    app = Twitter(username)
    # Get 20 Tweets of a user
    all_tweets = app.get_tweets()
    return all_tweets

def process_tweets(tweets):
    all_tweets = [tweet.to_dict() for tweet in tweets]
    # pandas dataframe
    df = pd.DataFrame(all_tweets)
    # filter
    filter_columns = ['created_on', 'text', 'likes','reply_counts', 'retweet_counts', 'id']
    df = df[filter_columns]
    return df

def twitter_scraper(input: Input) -> PerspectiveTable:
    """Returns latest 20 tweets of given usename, such as 'elonmusk'. """
    all_tweets = fetch_twitter_by_id(username=input.username)
    df = process_tweets(all_tweets)
    return PerspectiveTable(data=df)
