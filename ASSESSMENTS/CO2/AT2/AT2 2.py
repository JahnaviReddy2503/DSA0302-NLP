words = ["disagree", "agreement", "agreeable"]

print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<12} {:<12}".format(
    "Word","Prefix","Root","Suffix","Type","Meaning","Normalized"))

for word in words:

    prefix = "-"
    suffix = "-"
    meaning = ""

    if word.startswith("dis"):
        prefix = "dis"
        root = "agree"
        meaning = "Negative"
        mtype = "Derivational"

    elif word.endswith("ment"):
        root = "agree"
        suffix = "ment"
        meaning = "State"
        mtype = "Derivational"

    elif word.endswith("able"):
        root = "agree"
        suffix = "able"
        meaning = "Capable"
        mtype = "Derivational"

    print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<12} {:<12}".format(
        word,prefix,root,suffix,mtype,meaning,"agree"))
