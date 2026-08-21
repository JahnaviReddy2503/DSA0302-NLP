import re

text = input("Enter a text: ")

sentences = re.split(r'[.!?]', text)

last_noun = None

print("\nReference Resolution:")

for sentence in sentences:
    words = sentence.strip().split()

    for word in words:
        clean_word = word.lower().strip(",")
        
        if clean_word in ["he", "she", "it", "they", "him", "her", "them"]:
            if last_noun:
                print(word, "-->", last_noun)

        elif clean_word not in ["the", "a", "an", "is", "was", "and", "in", "to"]:
            last_noun = word