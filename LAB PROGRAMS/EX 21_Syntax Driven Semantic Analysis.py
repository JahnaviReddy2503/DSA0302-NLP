import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)
tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = RegexpParser(grammar)

tree = parser.parse(tags)

print("\nNoun Phrases and Meanings:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase, "-->", "Entity or Concept")