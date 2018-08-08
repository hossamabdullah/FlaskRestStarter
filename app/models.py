from enum import Enum


class Topic:
    def __init__(topicId, goodReviewNum, badReviewNum, sentimentResult ,updateDate,Sentence):
        self.topicId  = topicId 
        self.goodReviewNum = goodReviewNum
        self.badReviewNum = badReviewNum
        self.sentimentResult=sentimentResult
        self.updateDate=updateDate
        self.Sentence

class Sentence:
    def __init__(self, sentenceId, content, sentimentValue):
        self.sentenceId  = sentenceId 
        self.content = content
        self.sentimentValue = sentimentValue



class SentimentValues(Enum):
    GOOD = 1
    BAD = 0
