import numpy as np
def allLongestStrings(inputArray):
    A = np.array(inputArray)
    longstr = 0
    for j in range(A.shape[0]):
        if len(A.item(j)) > longstr:
            longstr = len(A.item(j))
    ls = []
    for i in range(A.shape[0]):
        if len(A.item(i)) < longstr:
            continue
        else:
            ls.append(A.item(i))
    return ls
