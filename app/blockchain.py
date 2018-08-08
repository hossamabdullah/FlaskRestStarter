import requests

class Blockchain:
    def __init__(self):
        pass

    def add_topic(self, keyword, sentiment_result, date):
        print("keyword to be sent: "+keyword+"\n")
        
        r = requests.post('http://localhost:3000/api/org.fagr.sentiment.Topic', 
        json={"$class": "org.fagr.sentiment.Topic",
        "topicId": str(date),
        "keyword":keyword,
        "goodReviewNum": sentiment_result['positive'],
        "badReviewNum": sentiment_result['negative'],
        "sentimentResult": sentiment_result['sentiment'],
        "updateDate": date})
        print("ya shiamaaaa"+ str(r.status_code))
        return r.status_code

    
    def add_sentiment(self,keyword, content, sentiment_result, date,ner):
        
        r = requests.post('http://localhost:3000/api/org.fagr.sentiment.Sentence', 
        json={"$class": "org.fagr.sentiment.Sentence",
        "$class": "org.fagr.sentiment.Sentence",
        "sentenceId":str(date),
        "content": content,
        "sentiment": sentiment_result['sentiment'],
        "NARKeywords": [ner],
        "topic": keyword})
        return r.status_code

if __name__ == '__main__':
    b = Blockchain()
    b.add_sentiment