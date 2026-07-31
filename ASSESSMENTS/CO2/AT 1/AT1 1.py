# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("{:<12} {:<10} {:<8} {:<15} {:<12}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        mtype = "Derivational"

    normalized = "connect"

    print("{:<12} {:<10} {:<8} {:<15} {:<12}".format(
        word, root, suffix, mtype, normalized))
