import tweepy
from tweepy import Stream                                   
from tweepy.streaming import StreamListener                 
from tweepy import OAuthHandler
import codecs
from string import punctuation
from flask import Flask, render_template, request

# The consumer key, consumer secret, access token and access secret should
# be obtained from the Twitter UI when registering an application
ckey = 'JjqU6C81ZSFttww8Xe2lWXrCg'
csecret = '7MQDARYlC3f7sX5TlstvEHI3BYVjTOiFvRtoiu8fpb5NjBSwny'
atoken = '835019765508788224-Twx0VMQM48xsdDV0OQ4Q1ZjGdmGrOTt'
asecret = 'N950rLZolhw3I1RLhzujjnqZXTRdu8yueS5HVoL62XLHh'

# OAuth Authentication
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Twitter API wrapper
api = tweepy.API(auth)

# Load the list of positive and negative words
# These will be used for analysing the tweets
pos_sent = open("positive-words.txt").read()
positive_words = pos_sent.split('\n')

neg_sent = open('negative-words.txt').read()
negative_words = neg_sent.split('\n')

# tweetSearch() searches for 100 tweets containing the "Celebrity name"
# and saves them to "testTweets.txt" for sentiment analysis at
# tweetSentimentAnalysis
def tweetSearch(celebrityName):

    outFile = codecs.open("testTweets.txt", 'w', "utf-8")
    results = api.search(q=celebrityName, lang="en", locale="en", count=100)

    for result in results:
        outFile.write(result.text + '\n')

    outFile.close()

#the core of the analysis logic
# count the total number
# of positive and negative words cumulated across all the
# tweets stored in "testTweets.txt" and decide the sentiment.
def posNegCount(tweet):

    pos = 0
    neg = 0

    for p in list(punctuation):
        tweet = tweet.replace(p, '')

    tweet = tweet.lower() #.encode('utf8')
    words = tweet.split(' ')
    word_count = len(words)

    for word in words:
        if word in positive_words:
            pos = pos + 1
        elif word in negative_words:
            neg = neg + 1

    return pos, neg

def tweetSentimentAnalysis():
    
    outFile = codecs.open("testTweetsLineByLine.txt", 'w', "utf-8")
    # Read all the tweets from "testTweets.txt" and 
    # split + store them to tweets_list
    tweets = codecs.open("testTweets.txt", 'r', "utf-8").read()
    tweets_list = tweets.split('\n')
    #tweets.close()           - AttributeError: 'str' object has no attribute 'close'

    positive_counter = 0
    negative_counter = 0

    # Call posNegCount() on each tweet stored in tweets_list and
    # increment positive_counter and negative_counter accordingly
    for idx, tweet in enumerate(tweets_list):
        if(len(tweet)):
            p, n = posNegCount(tweet)
            positive_counter += p
            negative_counter += n
            temp = p - n 
            dataToBeSaved = "tweet with idx : --- {}  --- \n , have the following postivity : {} \n\n".format(tweet, temp)
            #print(dataToBeSaved.encode("utf-8"))
            outFile.write(dataToBeSaved)
            
    outFile.close()

    if positive_counter > negative_counter:
        sentiment="POSITIVE"

    elif positive_counter < negative_counter:
        sentiment="NEGATIVE"

    else:
        sentiment="NEUTRAL"

    valuesSum=positive_counter+negative_counter
    output={'positive':positive_counter,'negative':negative_counter,'sentiment':sentiment,'valuesSum':valuesSum}


    print("//////////////////////////////////////////////////////////////////////////")
    print("positive_counter:", positive_counter, "negative_counter:", negative_counter,"valuesSum",valuesSum)
    print("//////////////////////////////////////////////////////////////////////////")
    # Hopefully, this is self-explanatory

    return (output)
