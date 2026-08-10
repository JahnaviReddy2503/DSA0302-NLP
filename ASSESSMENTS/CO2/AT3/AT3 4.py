from nltk.stem import PorterStemmer

ps=PorterStemmer()

words=["connected","connection","connecting","connectivity","studies","studied","studying","study","players","playing","replayed","unhappy","happiness"]

lemmas={
"connected":"connect",
"connection":"connection",
"connecting":"connect",
"connectivity":"connectivity",
"studies":"study",
"studied":"study",
"studying":"study",
"study":"study",
"players":"player",
"playing":"play",
"replayed":"replay",
"unhappy":"unhappy",
"happiness":"happiness"
}

types={
"connected":"Inflectional",
"connection":"Derivational",
"connecting":"Inflectional",
"connectivity":"Derivational",
"studies":"Inflectional",
"studied":"Inflectional",
"studying":"Inflectional",
"study":"Root",
"players":"Inflectional",
"playing":"Inflectional",
"replayed":"Inflectional",
"unhappy":"Derivational",
"happiness":"Derivational"
}

print("WORD -> STEM -> LEMMA -> TYPE")

for word in words:
    print(word,"->",ps.stem(word),"->",lemmas[word],"->",types[word])
