irregular={"children":"child","men":"man","women":"woman","mice":"mouse","feet":"foot","teeth":"tooth","people":"person","geese":"goose"}

def parser(word):
    word=word.lower()
    if word in irregular:
        return irregular[word],"Plural Noun"
    if word.endswith("ies") and len(word)>3:
        return word[:-3]+"y","Plural Noun"
    if word.endswith("ses") or word.endswith("xes") or word.endswith("zes") or word.endswith("ches") or word.endswith("shes"):
        return word[:-2],"Plural Noun"
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1],"Plural Noun"
    return word,"Singular Noun"

words=["car","cars","box","boxes","city","cities","child","children","watch","watches","bus","buses","book","books"]

print("WORD -> ROOT -> TYPE")

for word in words:
    root,tag=parser(word)
    print(word,"->",root,"->",tag)
