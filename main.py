from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from newspaper import Article

url = ''
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)

blob = TextBlob(text)
# French version
# blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
