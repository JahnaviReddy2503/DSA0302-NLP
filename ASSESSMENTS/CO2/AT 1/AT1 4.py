# Finite State Morphological Parser

words = ["writes", "writing", "written"]

print("{:<10} {:<30} {:<10} {:<10} {:<12}".format(
    "Word", "State Transition", "Root", "Pattern", "Normalized"))

for word in words:

    if word == "writes":
        transition = "Start -> write -> +s -> End"
        root = "write"
        pattern = "Regular"

    elif word == "writing":
        transition = "Start -> write -> +ing -> End"
        root = "write"
        pattern = "Regular"

    elif word == "written":
        transition = "Start -> write -> +en -> End"
        root = "write"
        pattern = "Irregular"

    print("{:<10} {:<30} {:<10} {:<10} {:<12}".format(
        word, transition, root, pattern, root))
