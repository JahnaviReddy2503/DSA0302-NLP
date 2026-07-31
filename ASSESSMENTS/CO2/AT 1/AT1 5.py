from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<12} {:<20} {:<12}".format(
    "Word", "Stem", "Normalized"))

for word in words:
    stem = ps.stem(word)
    print("{:<12} {:<20} {:<12}".format(
        word, stem, stem))
