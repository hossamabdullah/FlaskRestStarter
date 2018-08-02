from enum import Enum
# from mongoengine import Document
# from mongoengine.fields import StringField, DictField, ListField, IntField

# class Pet(Document):
#     id = IntField(primary_key=True)
#     category = DictField()
#     name = StringField()
#     photoUrls = ListField(StringField())
#     tags =  ListField(DictField())
#     status = StringField()


# class Topic:    
#     topicId=None
#     goodReviewNum=None
#     double badReviewNum=None
#     String sentimentResult=None
#     DateTime updateDate=None
#     Sentence=[] 

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
