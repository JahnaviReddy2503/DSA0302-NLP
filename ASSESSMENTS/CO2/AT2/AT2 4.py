words = ["activate", "activation", "reactivation"]

print("{:<15} {:<10} {:<10} {:<10} {:<20} {:<12}".format(
    "Word","Prefix","Root","Suffix","Sequence","Normalized"))

for word in words:

    prefix = "-"
    suffix = "-"

    if word == "activate":
        root = "activate"
        sequence = "Base"

    elif word == "activation":
        root = "activate"
        suffix = "ion"
        sequence = "activate + ion"

    elif word == "reactivation":
        prefix = "re"
        root = "activate"
        suffix = "ion"
        sequence = "re + activate + ion"

    print("{:<15} {:<10} {:<10} {:<10} {:<20} {:<12}".format(
        word,prefix,root,suffix,sequence,"activate"))
