from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing is a field of artificial intelligence",
    "Machine learning is used in artificial intelligence",
    "Natural language processing deals with text and language",
    "Computer vision deals with images"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, matrix).flatten()

ranking = scores.argsort()[::-1]

print("\nDocument Ranking:")

for index in ranking:
    print("Document", index + 1, "Score:", round(scores[index], 4))
    print(documents[index])
    print()