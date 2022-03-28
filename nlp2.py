from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

#nltk.download("stopwords")
from nltk.corpus import stopwords

stops = stopwords.words("english")

#print(stops)

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

#print(blob.word_counts["romeo"])

#print(blob.noun_phrases.count("lady capulet"))

more_stops = ["thee", "thy", "thou"]
stops += more_stops

items = blob.word_counts.items()

#print(items)

# use a list comprehension to eliminate tuples containing stop words

randj = [x for x in items if x[0] not in stops]
#print(randj[:10])

from operator import itemgetter

sorted_randj = sorted(randj)
#print(sorted_randj[:10])

sorted_randj = sorted(randj,key=itemgetter(1), reverse=True)
#print(sorted_randj[:10])

top20 = sorted_randj[:20]
df = pd.DataFrame(top20,columns=["words","count"])
print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="words", y="count", legend=False)

plt.gcf().tight_layout()
plt.show()