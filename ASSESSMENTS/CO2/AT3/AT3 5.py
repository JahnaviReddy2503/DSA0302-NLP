from nltk.stem import PorterStemmer
import re

ps=PorterStemmer()

text="""The organization organized an organizing meeting.
The organizer connected the system.
The connected devices were connecting successfully.
The studies were studied by researchers.
The players were playing games.
The companies developed new technologies."""

words=re.findall(r"[A-Za-z]+",text.lower())

print("WORD -> STEM")

for word in words:
    print(word,"->",ps.stem(word))

print("\nUNIQUE STEMS")

stems={ps.stem(word) for word in words}

for stem in sorted(stems):
    print(stem)
