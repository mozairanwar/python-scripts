def firstDuplicate(a):
    #dup = []
    dup = set() # It's much faster
    for i in range(0, len(a)):
        if a[i] in dup:
            return a[i]
        else:
            dup.add(a[i])
    return -1
