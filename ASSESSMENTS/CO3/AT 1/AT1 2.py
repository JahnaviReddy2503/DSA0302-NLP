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

uni=Counter()
bi=Counter()
tri=Counter()

for words in sentences:
    uni.update(words)
    bi.update(zip(words,words[1:]))
    tri.update(zip(words,words[1:],words[2:]))

total=sum(uni.values())

def p1(w):
    return uni[w]/total if uni[w] else 0

def p2(w1,w2):
    return bi[(w1,w2)]/uni[w1] if uni[w1] else 0

def p3(w1,w2,w3):
    return tri[(w1,w2,w3)]/bi[(w1,w2)] if bi[(w1,w2)] else 0

def backoff(w1,w2,w):
    if p3(w1,w2,w)>0:
        return p3(w1,w2,w)
    if p2(w2,w)>0:
        return p2(w2,w)
    return p1(w)

l1=0
l2=0
l3=0

for (w1,w2,w3),count in tri.items():
    a=(uni[w3]-1)/(total-1) if uni[w3]>1 else 0
    b=(bi[(w2,w3)]-1)/(uni[w2]-1) if bi[(w2,w3)]>1 and uni[w2]>1 else 0
    c=(count-1)/(bi[(w1,w2)]-1) if count>1 and bi[(w1,w2)]>1 else 0
    m=max(a,b,c)
    if m==a:
        l1+=count
    elif m==b:
        l2+=count
    else:
        l3+=count

s=l1+l2+l3

if s==0:
    l1=l2=l3=1/3
else:
    l1/=s
    l2/=s
    l3/=s

def interpolation(w1,w2,w):
    return l1*p1(w)+l2*p2(w2,w)+l3*p3(w1,w2,w)

sentence=input("Enter sentence: ").lower().split()

if len(sentence)<2:
    print("Enter at least two words")
else:
    w1=sentence[-2]
    w2=sentence[-1]
    vocabulary=[w for w in uni if w not in ["<s>","</s>"]]

    unsmoothed=[]
    backoff_results=[]
    interpolation_results=[]

    for w in vocabulary:
        unsmoothed.append((w,p3(w1,w2,w)))
        backoff_results.append((w,backoff(w1,w2,w)))
        interpolation_results.append((w,interpolation(w1,w2,w)))

    unsmoothed.sort(key=lambda x:x[1],reverse=True)
    backoff_results.sort(key=lambda x:x[1],reverse=True)
    interpolation_results.sort(key=lambda x:x[1],reverse=True)

    print("\nInterpolation Weights:")
    print("Unigram:",round(l1,3))
    print("Bigram:",round(l2,3))
    print("Trigram:",round(l3,3))

    print("\nUnsmoothed:")
    for w,p in unsmoothed[:5]:
        print(w,"->",round(p,4))

    print("\nBackoff:")
    for w,p in backoff_results[:5]:
        print(w,"->",round(p,4))

    print("\nDeleted Interpolation:")
    for w,p in interpolation_results[:5]:
        print(w,"->",round(p,4))
