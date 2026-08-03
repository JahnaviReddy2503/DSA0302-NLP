words = ["create", "creates", "creating"]

print("{:<12} {:<10} {:<15} {:<10} {:<12} {:<12}".format(
    "Word","Suffix","Grammar","Root","Normalized","Category"))

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"

    elif word.endswith("s"):
        suffix = "s"
        grammar = "3rd Person"

    elif word.endswith("ing"):
        suffix = "ing"
        grammar = "Present Participle"

    root = "create"

    print("{:<12} {:<10} {:<15} {:<10} {:<12} {:<12}".format(
        word,suffix,grammar,root,"create","Inflection"))
