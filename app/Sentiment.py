import tweepy
from tweepy import Stream                                   
from tweepy.streaming import StreamListener                 
from tweepy import OAuthHandler
import codecs
from string import punctuation
from flask import Flask, render_template, request
import nltk
from app.blockchain import Blockchain
import datetime

class Sentiment:
    def __init__(self):
        # The consumer key, consumer secret, access token and access secret should
        # be obtained from the Twitter UI when registering an application
        self.ckey = 'JjqU6C81ZSFttww8Xe2lWXrCg'
        self.csecret = '7MQDARYlC3f7sX5TlstvEHI3BYVjTOiFvRtoiu8fpb5NjBSwny'
        self.atoken = '835019765508788224-Twx0VMQM48xsdDV0OQ4Q1ZjGdmGrOTt'
        self.asecret = 'N950rLZolhw3I1RLhzujjnqZXTRdu8yueS5HVoL62XLHh'

        # OAuth Authentication
        self.auth = OAuthHandler(self.ckey, self.csecret)
        self.auth.set_access_token(self.atoken, self.asecret)

        # Twitter API wrapper
        self.api = tweepy.API(self.auth)

        # Load the list of positive and negative words
        # These will be used for analysing the tweets
        self.pos_sent = open("positive-words.txt", encoding="ISO-8859-1").read()
        self.positive_words = self.pos_sent.split('\n')

        self.neg_sent = open('negative-words.txt', encoding="ISO-8859-1").read()
        self.negative_words = self.neg_sent.split('\n')

    # tweetSearch() searches for 100 tweets containing the "Celebrity name"
    # and saves them to "testTweets.txt" for sentiment analysis at
    # tweetSentimentAnalysis
    def tweetSearch(self, celebrityName):

        self.keyword = celebrityName
        outFile = codecs.open("testTweets.txt", 'w', "utf-8")
        results = self.api.search(q=celebrityName, lang="en", locale="en", count=100)

        for result in results:
            outFile.write(result.text + '\n')

        outFile.close()

    #the core of the analysis logic
    # count the total number
    # of positive and negative words cumulated across all the
    # tweets stored in "testTweets.txt" and decide the sentiment.
    def nerfun(self, tweet):
        for sent in nltk.sent_tokenize(tweet):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    ner_result=chunk.label(), ' '.join(c[0] for c in chunk)
                    print("555555555555555555555555555555555555555555")
                    print(ner_result)
                    print("555555555555555555555555555555555555555555")
                    return ner_result


    def posNegCount(self, tweet):

        pos = 0
        neg = 0

        for p in list(punctuation):
            tweet = tweet.replace(p, '')

        tweet = tweet.lower() #.encode('utf8')
        words = tweet.split(' ')
        word_count = len(words)

        for word in words:
            if word in self.positive_words:
                pos = pos + 1
            elif word in self.negative_words:
                neg = neg + 1

        return pos, neg

    def tweetSentimentAnalysis(self):
        
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
                p, n = self.posNegCount(tweet)
                positive_counter += p
                negative_counter += n
                temp = p - n 
                dataToBeSaved = "tweet with idx : --- {}  --- \n , have the following postivity : {} \n\n".format(tweet, temp)
                #print(dataToBeSaved.encode("utf-8"))
                outFile.write(dataToBeSaved)

                ner=self.nerfun(tweet)
                
        outFile.close()

        if positive_counter > negative_counter:
            sentiment="POSITIVE"

        elif positive_counter < negative_counter:
            sentiment="NEGATIVE"

        else:
            sentiment="NEUTRAL"

        valuesSum=positive_counter+negative_counter
        output={'positive':positive_counter,'negative':negative_counter,'sentiment':sentiment,'valuesSum':valuesSum,'ner':ner}


        print("//////////////////////////////////////////////////////////////////////////")
        print("positive_counter:", positive_counter, "negative_counter:", negative_counter,"valuesSum",valuesSum)
        print("//////////////////////////////////////////////////////////////////////////")
        # Hopefully, this is self-explanatory
        blockchain = Blockchain()
        blockchain.add_topic(self.keyword, output, str(datetime.datetime.now()))
        
        return (output)
