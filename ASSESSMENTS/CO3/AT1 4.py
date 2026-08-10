from collections import Counter
import math

training_data=[
("the","DT"),("student","NN"),("is","VBZ"),("intelligent","JJ"),
("the","DT"),("student","NN"),("studies","VBZ"),("computer","NN"),("science","NN"),
("the","DT"),("teacher","NN"),("is","VBZ"),("helpful","JJ"),
("the","DT"),("teacher","NN"),("teaches","VBZ"),("python","NN"),
("they","PRP"),("are","VBP"),("working","VBG"),("quickly","RB"),
("students","NNS"),("learn","VB"),("python","NN"),
("students","NNS"),("study","VB"),("computer","NN"),
("in","IN"),("the","DT"),("class","NN")
]

word_tag_count=Counter()
tag_count=Counter()
transition_count=Counter()

for word,tag in training_data:
    word_tag_count[(word,tag)]+=1
    tag_count[tag]+=1

for i in range(len(training_data)-1):
    tag1=training_data[i][1]
    tag2=training_data[i+1][1]
    transition_count[(tag1,tag2)]+=1

tags=list(tag_count.keys())
lexicon={}

for word,tag in training_data:
    if word not in lexicon:
        lexicon[word]=tag

def rule_based(sentence):
    words=sentence.lower().split()
    result=[]
    for word in words:
        if word in lexicon:
            tag=lexicon[word]
        elif word.endswith("ly"):
            tag="RB"
        elif word.endswith("ing"):
            tag="VBG"
        elif word.endswith("ed"):
            tag="VBD"
        elif word.endswith("s"):
            tag="NNS"
        elif word in ["in","on","at","with","for","from"]:
            tag="IN"
        else:
            tag="NN"
        result.append((word,tag))
    return result

def emission_probability(word,tag):
    return (word_tag_count[(word,tag)]+1)/(tag_count[tag]+len(word_tag_count))

def transition_probability(previous_tag,current_tag):
    return (transition_count[(previous_tag,current_tag)]+1)/(tag_count[previous_tag]+len(tags))

def stochastic(sentence):
    words=sentence.lower().split()
    if not words:
        return []
    dp=[{} for _ in words]
    for tag in tags:
        score=math.log(emission_probability(words[0],tag))
        dp[0][tag]=(score,[tag])
    for i in range(1,len(words)):
        for current_tag in tags:
            best_score=float("-inf")
            best_path=None
            emission=math.log(emission_probability(words[i],current_tag))
            for previous_tag in dp[i-1]:
                transition=math.log(transition_probability(previous_tag,current_tag))
                score=dp[i-1][previous_tag][0]+transition+emission
                if score>best_score:
                    best_score=score
                    best_path=dp[i-1][previous_tag][1]+[current_tag]
            dp[i][current_tag]=(best_score,best_path)
    best_tag=max(dp[-1],key=lambda tag:dp[-1][tag][0])
    return list(zip(words,dp[-1][best_tag][1]))

def transformation_based(sentence):
    result=rule_based(sentence)
    for i in range(1,len(result)):
        word,tag=result[i]
        previous_word,previous_tag=result[i-1]
        if previous_tag=="PRP" and tag=="NN":
            result[i]=(word,"VB")
        elif previous_tag in ["VBZ","VBP"] and tag=="NN":
            result[i]=(word,"VB")
    return result

sentence=input("Enter an English sentence: ")

print("\n========== RULE-BASED TAGGING ==========")
for word,tag in rule_based(sentence):
    print(word,"->",tag)

print("\n========== STOCHASTIC TAGGING ==========")
for word,tag in stochastic(sentence):
    print(word,"->",tag)

print("\n========== TRANSFORMATION-BASED TAGGING ==========")
for word,tag in transformation_based(sentence):
    print(word,"->",tag)

print("\n========== PENN TREEBANK TAGSET ==========")
print("NN = Noun")
print("NNS = Plural Noun")
print("VB = Verb")
print("VBD = Past Tense Verb")
print("VBG = Verb Gerund")
print("VBP = Non-3rd Person Verb")
print("VBZ = 3rd Person Verb")
print("JJ = Adjective")
print("RB = Adverb")
print("PRP = Personal Pronoun")
print("DT = Determiner")
print("IN = Preposition")
