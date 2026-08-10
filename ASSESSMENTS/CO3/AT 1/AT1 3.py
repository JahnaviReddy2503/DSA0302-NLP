from collections import Counter
import math

training_corpus=[
"the student is intelligent",
"the student is hardworking",
"the student is studying",
"the student is learning",
"the teacher is helpful",
"the teacher is intelligent",
"the teacher is teaching",
"the student learns python",
"the student learns programming",
"students study computer science"
]

test_corpus=[
"the student is intelligent",
"the teacher is helpful",
"the student learns python",
"students study computer science"
]

uni=Counter()
bi=Counter()
tri=Counter()

for sentence in training_corpus:
    words=["<s>"]+sentence.lower().split()+["</s>"]
    for word in words:
        uni[word]+=1
    for i in range(len(words)-1):
        bi[(words[i],words[i+1])]+=1
    for i in range(len(words)-2):
        tri[(words[i],words[i+1],words[i+2])]+=1

total=sum(uni.values())
vocabulary=set(uni.keys())
V=len(vocabulary)

def unigram_probability(word):
    return uni[word]/total if uni[word]>0 else 0

def bigram_probability(w1,w2):
    if uni[w1]==0:
        return 0
    return bi[(w1,w2)]/uni[w1]

def trigram_probability(w1,w2,w3):
    if bi[(w1,w2)]==0:
        return 0
    return tri[(w1,w2,w3)]/bi[(w1,w2)]

def smoothed_unigram(word):
    return (uni[word]+1)/(total+V)

def smoothed_bigram(w1,w2):
    return (bi[(w1,w2)]+1)/(uni[w1]+V)

def smoothed_trigram(w1,w2,w3):
    return (tri[(w1,w2,w3)]+1)/(bi[(w1,w2)]+V)

def calculate_entropy(probabilities):
    if len(probabilities)==0:
        return float("inf")
    total_log=0
    for p in probabilities:
        if p<=0:
            return float("inf")
        total_log+=math.log2(p)
    return -total_log/len(probabilities)

uni_probs=[]
bi_probs=[]
tri_probs=[]
smooth_uni_probs=[]
smooth_bi_probs=[]
smooth_tri_probs=[]

for sentence in test_corpus:
    words=sentence.lower().split()

    for word in words:
        uni_probs.append(unigram_probability(word))
        smooth_uni_probs.append(smoothed_unigram(word))

    words_bi=["<s>"]+words
    for i in range(len(words_bi)-1):
        w1=words_bi[i]
        w2=words_bi[i+1]
        bi_probs.append(bigram_probability(w1,w2))
        smooth_bi_probs.append(smoothed_bigram(w1,w2))

    words_tri=["<s>"]+words
    for i in range(len(words_tri)-2):
        w1=words_tri[i]
        w2=words_tri[i+1]
        w3=words_tri[i+2]
        tri_probs.append(trigram_probability(w1,w2,w3))
        smooth_tri_probs.append(smoothed_trigram(w1,w2,w3))

H_uni=calculate_entropy(uni_probs)
H_bi=calculate_entropy(bi_probs)
H_tri=calculate_entropy(tri_probs)
H_smooth_uni=calculate_entropy(smooth_uni_probs)
H_smooth_bi=calculate_entropy(smooth_bi_probs)
H_smooth_tri=calculate_entropy(smooth_tri_probs)

print("\n========== UNSMOOTHED ENTROPY ==========")
print("Unigram Entropy :",round(H_uni,4))
print("Bigram Entropy  :",round(H_bi,4))
print("Trigram Entropy :",round(H_tri,4))

print("\n========== ADD-ONE SMOOTHED ENTROPY ==========")
print("Unigram Entropy :",round(H_smooth_uni,4))
print("Bigram Entropy  :",round(H_smooth_bi,4))
print("Trigram Entropy :",round(H_smooth_tri,4))

print("\n========== SENTENCE ANALYSIS ==========")

for sentence in test_corpus:
    words=sentence.lower().split()
    probabilities=[]
    for word in words:
        probabilities.append(smoothed_unigram(word))
    h=calculate_entropy(probabilities)
    print(sentence,"->",round(h,4))
