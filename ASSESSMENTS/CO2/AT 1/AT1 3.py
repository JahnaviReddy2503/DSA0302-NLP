# Stemming Based Preprocessing

words = ["played", "player", "playing"]

print("{:<10} {:<10} {:<12} {:<15} {:<10}".format(
    "Word", "Stem", "Affix", "Type", "Normalized"))

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"

    print("{:<10} {:<10} {:<12} {:<15} {:<10}".format(
        word, stem, affix, t, stem))
