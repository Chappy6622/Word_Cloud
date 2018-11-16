# noinspection PyUnresolvedReferences
import collections
import numpy as np
from os import path
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


file = open('98-0.txt')

stopwords = set(line.strip() for line in open ('stopwords'))

punc = set(line.strip() for line in open ('punctuation'))

wordcount = { }


for word in file.read().lower().split():
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

for w in wordcount:
    for p in punc:
        if w == p:
            w = w.replace(p, "")

d = collections.Counter(wordcount)
sorted(d.values())

for word, count in d.most_common(10):
    print(word, ": ", count)

somestring = " "
for w in d:
    somestring += w

wordcloud = WordCloud().generate(somestring)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()