import nltk
from textblob import TextBlob
from newspaper import Article


url = 'https://www.hindustantimes.com/india-news/afternoon-briefing-india-denies-bangladesh-flooding-due-to-tripura-dam-abhishek-banerjee-breaks-silence-and-more-101724311439313.html'
article = Article(url)

article.download()
article.parse()
article.nlp()
text = article.summary
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
