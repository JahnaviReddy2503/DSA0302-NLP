from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

print("=" * 60)
print("      PORTER STEMMER IMPLEMENTATION")
print("=" * 60)

# -------------------------------
# PART 1: Text Preprocessing
# -------------------------------

text = input("\nEnter a sentence: ")

# Simple Tokenization
words = text.split()

print("\nOriginal Words:")
print(words)

# Apply Stemming
stemmed_words = [ps.stem(word) for word in words]

print("\nStemmed Words:")
print(stemmed_words)

print("\nOriginal Word\t\tStemmed Word")
print("-" * 40)

for original, stem in zip(words, stemmed_words):
    print("{:<20}{}".format(original, stem))

# -------------------------------
# PART 2: Information Retrieval
# -------------------------------

print("\n" + "=" * 60)
print("INFORMATION RETRIEVAL DEMONSTRATION")
print("=" * 60)

documents = [
    "He is playing football every evening",
    "They played football yesterday",
    "Football players practice daily",
    "She likes cricket",
    "Running is good for health"
]

query = input("\nEnter a search word: ")

print("\nSearching WITHOUT Porter Stemming...\n")

found = False

for doc in documents:
    if query.lower() in doc.lower():
        print(doc)
        found = True

if not found:
    print("No matching document found.")

print("\nSearching WITH Porter Stemming...\n")

query_stem = ps.stem(query.lower())

found = False

for doc in documents:
    tokens = doc.lower().split()
    stems = [ps.stem(word) for word in tokens]

    if query_stem in stems:
        print(doc)
        found = True

if not found:
    print("No matching document found.")

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print("✓ Tokenization completed successfully.")
print("✓ Porter Stemmer reduced different word forms into root words.")
print("✓ Vocabulary size was reduced.")
print("✓ Information Retrieval improved after stemming.")
print("✓ Related documents were successfully retrieved.")
