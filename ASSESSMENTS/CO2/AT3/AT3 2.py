def parse(word):
    prefixes=["un","re"]
    suffixes=["able","iest","ing","est","s"]
    prefix=""
    suffix=""
    root=word

    for p in prefixes:
        if root.startswith(p) and len(root)>len(p)+2:
            prefix=p
            root=root[len(p):]
            break

    if root.endswith("iest"):
        suffix="est"
        root=root[:-4]+"y"
    elif root.endswith("able"):
        suffix="able"
        root=root[:-4]
    elif root.endswith("ing"):
        suffix="ing"
        root=root[:-3]
        if root.endswith(root[-1]):
            root=root[:-1]
    elif root.endswith("est"):
        suffix="est"
        root=root[:-3]
    elif root.endswith("s") and not root.endswith("ss"):
        suffix="s"
        root=root[:-1]

    return prefix,root,suffix

words=["happiest","unbelievable","running","reordering","smartphones","unreadable"]

for word in words:
    prefix,root,suffix=parse(word)
    print(word,"->",end=" ")
    if prefix:
        print(prefix,"+",end=" ")
    print(root,end="")
    if suffix:
        print("+",suffix)
    else:
        print()

print("\nFST STATES")
print("START -> PREFIX -> ROOT -> SUFFIX -> END")
