import csv
import re
import sys

import tweepy
from textblob import TextBlob

# Step 1 - Autenticacion con el api de twiter
consumer_key = 'OoKtdnkn2PhPdVopgcPPVszBL'
consumer_secret = 'zJCI08nnQ7wGiosCOe7Udbu4PlpchanXFbjytZZJFkontr2wOC'

access_token = '572213920-pfExxBDxG4W7gu6ke8Yh1xexYcypE9QOddfvpY6u'
access_token_secret = 'C2tOsrGpF48uBoxVjcyHYptljLpfAesln2ABZacpLy1mL'

# Step 2 - pasamos parametros
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 3 - los re-twiter buscando
query = '#HackathonParlamentario'
public_tweets = api.search(query, count=200)


# Step 4 - Separamos los twiter
def clean_tweet(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return tweet


# Step 5 - Segundo parametros
f = open("hola.csv", 'wt')
try:
    # Step 5.0 - guardamos
    writer = csv.writer(f)
    writer.writerow(('Tweet', 'Sentiment'))

    # Step 5.1 - recorremos los tweets
    positive = 0
    negative = 0
    neutro = 0

    for tweet in public_tweets:
        cleaned_tweet = clean_tweet(tweet.text)
        _analysis = TextBlob(cleaned_tweet)
        print(_analysis.sentiment.polarity)
        # Step 5.2 - si verifica polaridad
        if (_analysis.sentiment.polarity > 0):
            sentiment = 'POSITIVE'
            positive += 1

        elif (_analysis.sentiment.polarity == 0):
            sentiment = 'NEUTRAL'
            neutro += 1
        else:
            sentiment = 'NEGATIVE'
            negative += 1
        writer.writerow((cleaned_tweet, sentiment))

    print("Positive tweets percentage: {} %".format(100 * positive / len(public_tweets)))
    print("Negative tweets percentage: {} %".format(100 * negative / len(public_tweets)))
    print("Neutral tweets percentage: {} %".format(100 * neutro / len(public_tweets)))

finally:
    f.close()





#
#
# import re
# import tweepy
# from tweepy import OAuthHandler
# from textblob import TextBlob
#
#
# class TwitterClient(object):
#     '''
#     Generic Twitter Class for sentiment analysis.
#     '''
#
#     def __init__(self):
#         '''
#         Class constructor or initialization method.
#         '''
#         # keys and tokens from the Twitter Dev Console
#
#         # consumer_key = ''
#         # consumer_secret = ''
#         # access_token = ''
#         # access_token_secret = ''
#
#         consumer_key = 'OoKtdnkn2PhPdVopgcPPVszBL'
#         consumer_secret = 'zJCI08nnQ7wGiosCOe7Udbu4PlpchanXFbjytZZJFkontr2wOC'
#
#         access_token = '572213920-pfExxBDxG4W7gu6ke8Yh1xexYcypE9QOddfvpY6u'
#         access_token_secret = 'C2tOsrGpF48uBoxVjcyHYptljLpfAesln2ABZacpLy1mL'
#
#         # attempt authentication
#         try:
#             # create OAuthHandler object
#             self.auth = OAuthHandler(consumer_key, consumer_secret)
#             # set access token and secret
#             self.auth.set_access_token(access_token, access_token_secret)
#             # create tweepy API object to fetch tweets
#             self.api = tweepy.API(self.auth)
#         except:
#             print("Error: Authentication Failed")
#
#     def clean_tweet(self, tweet):
#         '''
#         Utility function to clean tweet text by removing links, special characters
#         using simple regex statements.
#         '''
#         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())
#
#     def get_tweet_sentiment(self, tweet):
#         '''
#         Utility function to classify sentiment of passed tweet
#         using textblob's sentiment method
#         '''
#         # create TextBlob object of passed tweet text
#         analysis = TextBlob(self.clean_tweet(tweet))
#         # set sentiment
#         if analysis.sentiment.polarity > 0:
#             return 'positive'
#         elif analysis.sentiment.polarity == 0:
#             return 'neutral'
#         else:
#             return 'negative'
#
#     def get_tweets(self, query, count=10):
#         '''
#         Main function to fetch tweets and parse them.
#         '''
#         # empty list to store parsed tweets
#         tweets = []
#
#         try:
#             # call twitter api to fetch tweets
#             fetched_tweets = self.api.search(q=query, count=count)
#
#             # parsing tweets one by one
#             for tweet in fetched_tweets:
#                 # empty dictionary to store required params of a tweet
#                 parsed_tweet = {}
#
#                 # saving text of tweet
#                 parsed_tweet['text'] = tweet.text
#                 # saving sentiment of tweet
#                 parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
#
#                 # appending parsed tweet to tweets list
#                 if tweet.retweet_count > 0:
#                     # if tweet has retweets, ensure that it is appended only once
#                     if parsed_tweet not in tweets:
#                         tweets.append(parsed_tweet)
#                 else:
#                     tweets.append(parsed_tweet)
#
#             # return parsed tweets
#             return tweets
#
#         except tweepy.TweepError as e:
#             # print error (if any)
#             print("Error : " + str(e))
#
#
# def main():
#     # creating object of TwitterClient Class
#     api = TwitterClient()
#     # calling function to get tweets
#     query = 'HackathonParlamentario'
#     tweets = api.get_tweets(query=query, count=200)
#     print("Query : ", query)
#
#     # picking positive tweets from tweets
#     ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
#     # percentage of positive tweets
#     print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
#     # picking negative tweets from tweets
#     ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
#     # percentage of negative tweets
#     print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
#     # percentage of neutral tweets
#     neutral_tweets = len(tweets) - len(ntweets) - len(ptweets)
#     print("Neutral tweets percentage: {} %".format(100 * neutral_tweets / len(tweets)))
#
#     # printing first 5 positive tweets
#     print("\n\nPositive tweets:")
#     for tweet in ptweets[:10]:
#         print(tweet['text'])
#
#     # printing first 5 negative tweets
#     print("\n\nNegative tweets:")
#     for tweet in ntweets[:10]:
#         print(tweet['text'])
#
#
# if __name__ == "__main__":
#     # calling main function
#     main()