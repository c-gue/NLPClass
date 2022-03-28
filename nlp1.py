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

from textblob import Word

index = Word('index')
cacti = Word('cacti')

print(index.pluralize())
print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


#Spellcheck and corrections
word = Word("theyr")
print(word.spellcheck())

print(word.correct())

word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

#print(word1.lemmatize())
#print(word2.lemmatize())

happy = Word('happy')

print(happy.definition())
#print(happy.synsets)