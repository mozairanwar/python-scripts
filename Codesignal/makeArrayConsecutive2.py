def makeArrayConsecutive2(statues):
    statues.sort()
    statue=0
    for i in range(len(statues)-1):
        diff=statues[i+1]-statues[i]
        if diff>1:
            statue=statue+(diff-1)
    return statue
