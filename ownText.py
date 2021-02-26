from textblob import TextBlob

with open('scratch.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
# French version
# blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
