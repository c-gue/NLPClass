from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags)

#print(blob.noun_phrases)
#Polarity is positive vs negative. Subjectivity is how subjective the phrase is.
#Both are measured -1 to 1
#print(blob.sentiment)
#print("Polarity:",blob.sentiment.polarity)
#print("Subjectivity:",blob.sentiment.subjectivity)
#for sentence in sentences:
    #print(sentence,':', round(sentence.sentiment.polarity,3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)


spanish = blob.translate(to='es')
print(spanish)

chinese = blob.translate(to="zh")
print(chinese)

french = blob.translate(to='fr')
print(french)

hindi = blob.translate(to='ne')
print(hindi)

english = hindi.translate(to='en')
print(english)