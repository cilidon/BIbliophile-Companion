from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#opens the file. the with statement here will automatically close it afterwards.
filen="C:/Users/manda/Desktop/newpuretxt.txt"
with open(filen) as input_file:
    #build a counter from each word in the file
    count = Counter(word for line in input_file
                            for word in line.split() if not word in stopwords.words())

top_3_title=[seq[0] for seq in count.most_common(3)]
#print(count.most_common(3)[2])
print(top_3_title)
print(top_3_title[1])

