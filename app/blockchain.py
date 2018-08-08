from app import app
import requests
import datetime 


class Blockchain:
    def __init__(self):
        # self.API = "http://localhost:3000/api"
        self.API = app.config["API_URL"]

    def add_topic(self, id, keyword, sentiment_result, date):
        print("keyword to be sent: "+keyword+"\n")
        
        r = requests.post(self.API+'/org.fagr.sentiment.Topic', 
        json={"$class": "org.fagr.sentiment.Topic",
        "topicId": id,
        "keyword":keyword,
        "goodReviewNum": sentiment_result['positive'],
        "badReviewNum": sentiment_result['negative'],
        "sentimentResult": sentiment_result['sentiment'],
        "updateDate": date})
        print("ya shiamaaaa"+ str(r.status_code))
        return r.status_code

    
    def add_sentence(self, id, content, sentiment_result, date, ner, topicModelingValues, topicId):
        topicId = "resource:org.fagr.sentiment.Topic#" + topicId
        r = requests.post(self.API+'/org.fagr.sentiment.Sentence', 
        json={"$class": "org.fagr.sentiment.Sentence",
        "$class": "org.fagr.sentiment.Sentence",
        "sentenceId":id,
        "content": content,
        "sentiment": sentiment_result,
        "NERKeywords": [ner],
        "TopicModelingValues": [topicModelingValues],
        "topic": topicId})
        return r.status_code

    def return_topic(self,keyword):
        print("keyword to be sent: "+keyword+"\n")
        keyword={'keyword':keyword}
        r = requests.get(self.API+'/queries/selectAssetByOwner',params=keyword)
        return r.json()

    def return_sentence(self,topicId):
        keyword = "resource:org.fagr.sentiment.Topic#" + topicId
        print("keyword to be sent: "+keyword+"\n")
        keyword={'topic':keyword}
        r = requests.get(self.API+'/queries/selectAssetByType',params=keyword)
        return r.json()



if __name__ == '__main__':
    b = Blockchain()
    sentiment = {"sentiment": "POSITIVE", "positive": "4", "negative": "2"}

    # status_code = b.add_topic(12, "vodafone", sentiment, str(datetime.datetime.now()))
    # print(status_code)
    # status_code = b.add_sentence(11, "vodafone", "shimaa", sentiment, str(datetime.datetime.now()), "", "resource:org.fagr.sentiment.Topic#12")
    # print(status_code)

    # status_code=b.return_topic("vodafone")
    # print(status_code)

    status_code=b.return_sentence("12")
    print(status_code)
