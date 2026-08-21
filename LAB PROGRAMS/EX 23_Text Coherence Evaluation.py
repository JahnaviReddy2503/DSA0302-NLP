import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = input("Enter a text: ")

sentences = sent_tokenize(text)

stop_words = set(stopwords.words("english"))

sets = []

for sentence in sentences:
    words = word_tokenize(sentence.lower())
    words = set(word for word in words if word.isalpha() and word not in stop_words)
    sets.append(words)

scores = []

for i in range(len(sets) - 1):
    if sets[i] and sets[i + 1]:
        similarity = len(sets[i] & sets[i + 1]) / len(sets[i] | sets[i + 1])
        scores.append(similarity)

if scores:
    coherence = sum(scores) / len(scores)
else:
    coherence = 0

print("\nCoherence Score:", round(coherence, 2))

if coherence >= 0.2:
    print("Text is Coherent")
else:
    print("the Text is Less Coherent")