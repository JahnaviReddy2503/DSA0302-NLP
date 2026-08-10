from collections import Counter

corpus=[
"the student is intelligent",
"the student is hardworking",
"the student is studying",
"the student is learning",
"the student learns python",
"the student learns programming",
"the teacher is helpful",
"the teacher is intelligent",
"the teacher teaches python",
"the teacher teaches programming",
"students learn quickly",
"students study computer science"
]

sentences=[["<s>"]+s.lower().split()+["</s>"] for s in corpus]

unigram=Counter()
bigram=Counter()
trigram=Counter()

for words in sentences:
    unigram.update(words)
    bigram.update(zip(words,words[1:]))
    trigram.update(zip(words,words[1:],words[2:]))

total=sum(unigram.values())

def p1(w):
    return unigram[w]/total if unigram[w] else 0

def p2(w1,w2):
    return bigram[(w1,w2)]/unigram[w1] if unigram[w1] else 0

def p3(w1,w2,w3):
    return trigram[(w1,w2,w3)]/bigram[(w1,w2)] if bigram[(w1,w2)] else 0

sentence=input("Enter incomplete sentence: ").lower().split()
n=int(input("Enter N (1,2 or 3): "))

vocabulary=[w for w in unigram if w not in ["<s>","</s>"]]
predictions=[]

if n==1:
    for w in vocabulary:
        predictions.append((w,p1(w)))
elif n==2:
    for w in vocabulary:
        prob=p2(sentence[-1],w)
        if prob>0:
            predictions.append((w,prob))
elif n==3:
    if len(sentence)>=2:
        for w in vocabulary:
            prob=p3(sentence[-2],sentence[-1],w)
            if prob>0:
                predictions.append((w,prob))
else:
    print("Invalid N")

predictions.sort(key=lambda x:x[1],reverse=True)

print("\nTop-5 Predictions:")
for w,p in predictions[:5]:
    print(w,"->",round(p,4))

print("\nUnseen N-gram:")
print("P(programming|student,is) =",p3("student","is","programming"))
