words = ["analyzing", "analysis", "analytical"]

print("{:<12} {:<10} {:<10} {:<15} {:<12}".format(
    "Word", "Root", "Affix", "Type", "Normalized"))

for word in words:

    if word.endswith("ing"):
        root = "analyze"
        affix = "ing"
        mtype = "Inflectional"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "sis"
        mtype = "Derivational"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "ical"
        mtype = "Derivational"

    print("{:<12} {:<10} {:<10} {:<15} {:<12}".format(
        word, root, affix, mtype, "analyze"))
