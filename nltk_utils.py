import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer=PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
    
    pass

def stemming(word):
    return stemmer.stem(word.lower())
    pass

def bag_of_words(tokenize_sentence,all_words):
    pass

#test for tokenising
a="Is anyone there"
print(a)
a=tokenize(a)
print(a)

#test for the stemming
words=["history","historical","histogram"]
stemmed_words=[stemming(w)for w in words]
print(stemmed_words)