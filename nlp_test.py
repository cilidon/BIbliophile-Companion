import nltk
import sys

text="hey men what's up? cats feet "

#tokenization

#tokenizer=nltk.tokenize.WhitespaceTokenizer()
#tokenizer=nltk.tokenize.WordPunctTokenizer()
tokenizer=nltk.tokenize.TreebankWordTokenizer()
tokens=tokenizer.tokenize(text)
print(tokens)

#stemming

stemmer=nltk.stem.PorterStemmer()
stemm=" ".join(stemmer.stem(token) for token in tokens)
#stemmer=nltk.stem.WordNetLemmatizer()
#" ".join(stemmer.lemmatize(token) for token in tokens)
print(stemm)

