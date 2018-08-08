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
    def __init__(self, id, content, sentiment_result, date, ner, topicModelingValues, topicId):
        self.id  = id 
        self.content = content
        self.sentiment_result = sentiment_result
        self.date = date
        self.ner = ner
        self.topicModelingValues = topicModelingValues
        self.topicId = topicId



class SentimentValues(Enum):
    GOOD = 1
    BAD = 0
