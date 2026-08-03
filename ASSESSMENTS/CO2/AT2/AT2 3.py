words = ["govern", "government", "governance"]

print("{:<15} {:<10} {:<10} {:<20} {:<12}".format(
    "Word","Root","Affix","Derivation","Normalized"))

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Base"

    elif word.endswith("ment"):
        root = "govern"
        affix = "ment"
        level = "Level 1"

    elif word.endswith("ance"):
        root = "govern"
        affix = "ance"
        level = "Level 1"

    print("{:<15} {:<10} {:<10} {:<20} {:<12}".format(
        word,root,affix,level,"govern"))
