from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags)

print(blob.noun_phrases)


