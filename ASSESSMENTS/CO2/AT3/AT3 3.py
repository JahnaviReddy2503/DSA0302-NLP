from collections import Counter
import math
import time

documents=[
"technology companies develop new software",
"computer technology improves digital systems",
"software companies release new applications",
"new technology creates digital products",
"computer software supports modern technology",
"business companies increase market revenue",
"financial markets improve business growth",
"companies report higher business profits",
"business markets show strong financial growth",
"companies invest in financial markets"
]

labels=["technology","technology","technology","technology","technology","business","business","business","business","business"]

def tokenize(text):
    return text.lower().split()

def stem(word):
    for suffix in ["ing","ed","ies","s"]:
        if word.endswith(suffix) and len(word)>len(suffix)+2:
            if suffix=="ies":
                return word[:-3]+"y"
            return word[:-len(suffix)]
    return word

def lemmatize(word):
    rules={
        "companies":"company",
        "technologies":"technology",
        "applications":"application",
        "systems":"system",
        "markets":"market",
        "profits":"profit",
        "improves":"improve",
        "creates":"create",
        "invest":"invest"
    }
    return rules.get(word,word)

def preprocess(doc,method):
    words=tokenize(doc)
    if method=="original":
        return words
    if method=="stem":
        return [stem(w) for w in words]
    return [lemmatize(w) for w in words]

def vectorize(train,test):
    vocabulary=sorted(set(w for doc in train for w in doc))
    train_vectors=[]
    test_vectors=[]
    for doc in train:
        count=Counter(doc)
        train_vectors.append([count[w] for w in vocabulary])
    for doc in test:
        count=Counter(doc)
        test_vectors.append([count[w] for w in vocabulary])
    return vocabulary,train_vectors,test_vectors

def predict(train_vectors,train_labels,test_vector):
    scores={}
    for label in set(train_labels):
        scores[label]=0
    for label in scores:
        vectors=[v for v,l in zip(train_vectors,train_labels) if l==label]
        scores[label]=sum(sum(a*b for a,b in zip(v,test_vector)) for v in vectors)
    return max(scores,key=scores.get)

split=7

train_docs=documents[:split]
test_docs=documents[split:]
train_labels=labels[:split]
test_labels=labels[split:]

for method in ["original","stem","lemma"]:
    start=time.time()
    train=[preprocess(d,method) for d in train_docs]
    test=[preprocess(d,method) for d in test_docs]
    vocabulary,train_vectors,test_vectors=vectorize(train,test)
    predictions=[]
    for vector in test_vectors:
        predictions.append(predict(train_vectors,train_labels,vector))
    correct=sum(p==a for p,a in zip(predictions,test_labels))
    accuracy=correct/len(test_labels)*100
    elapsed=time.time()-start
    print("\n",method.upper())
    print("Vocabulary Size:",len(vocabulary))
    print("Predictions:",predictions)
    print("Actual:",test_labels)
    print("Accuracy:",round(accuracy,2),"%")
    print("Processing Time:",round(elapsed,6),"seconds")
