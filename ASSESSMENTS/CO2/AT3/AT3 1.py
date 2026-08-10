from nltk.stem import PorterStemmer
import re

ps=PorterStemmer()

text="infection infectious infected infect infections infecting"

words=re.findall(r"[A-Za-z]+",text.lower())

print("WORD -> STEM")
for word in words:
    print(word,"->",ps.stem(word))

print("\nMORPHOLOGICAL ANALYSIS")
analysis={
"infection":"infect + ion",
"infectious":"infect + ious",
"infected":"infect + ed",
"infect":"infect",
"infections":"infect + ion + s",
"infecting":"infect + ing"
}

for word in words:
    print(word,"->",analysis.get(word,"Unknown"))

print("\nDERIVATIONAL: -ion, -ious")
print("INFLECTIONAL: -ed, -ing, -s")
