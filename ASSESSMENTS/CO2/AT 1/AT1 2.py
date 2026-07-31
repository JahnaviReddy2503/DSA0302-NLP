# Morphological Parsing

words = ["unhappy", "happiness", "happily"]

print("{:<12} {:<8} {:<10} {:<8} {:<15} {:<10}".format(
    "Word", "Prefix", "Base", "Suffix", "Type", "Root"))

for word in words:

    if word.startswith("un"):
        prefix = "un"
        base = "happy"
        suffix = "-"
        mtype = "Derivational"

    elif word.endswith("ness"):
        prefix = "-"
        base = "happy"
        suffix = "ness"
        mtype = "Derivational"

    elif word.endswith("ly"):
        prefix = "-"
        base = "happy"
        suffix = "ly"
        mtype = "Derivational"

    print("{:<12} {:<8} {:<10} {:<8} {:<15} {:<10}".format(
        word, prefix, base, suffix, mtype, base))
