from nltk.stem import PorterStemmer
import re
import time

stemmer=PorterStemmer()

documents=[
"running runners runs",
"studies studied studying",
"organization organized organizer",
"technology technologies technological",
"companies company business businesses",
"connected connecting connection"
]

def tokenize(text):
    return re.findall(r"[A-Za-z]+",text.lower())

def preprocess(text):
    return " ".join(stemmer.stem(word) for word in tokenize(text))

print("ORIGINAL DOCUMENTS")

for doc in documents:
    print(doc)

start=time.time()

processed=[preprocess(doc) for doc in documents]

vocab_before=set()

for doc in documents:
    vocab_before.update(tokenize(doc))

vocab_after=set()

for doc in processed:
    vocab_after.update(doc.split())

processing_time=time.time()-start

print("\nSTEMMED DOCUMENTS")

for doc in processed:
    print(doc)

print("\nVOCABULARY COMPARISON")
print("Vocabulary Before Stemming:",len(vocab_before))
print("Vocabulary After Stemming:",len(vocab_after))

print("\nORIGINAL VOCABULARY")
print(sorted(vocab_before))

print("\nSTEMMED VOCABULARY")
print(sorted(vocab_after))

print("\nPROCESSING TIME:",round(processing_time,6),"seconds")
