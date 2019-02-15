from textblob import TextBlob

data = TextBlob(u'Hi i am angry on you ,as bad as have a bad opinion on u')
print(data.tags)
print(data.words)
print(data.sentiment.polarity)
print(data.translate(to = 'te'))