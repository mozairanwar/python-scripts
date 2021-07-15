"""def first_bad_element(sequence):
    Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1.
    for i in range(len(sequence)-1):
        if sequence[i] / sequence[i+1] >= 1:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = first_bad_element(sequence)
    if j == -1:
        return True
    if first_bad_element(sequence[j-1:j] + sequence[j+1:]) == -1: 
        return True # Removed i element
    if first_bad_element(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True # Removed i+1 element
    return False"""

def first_bad_element(sequence, k):
    if 0 < k < len(sequence) - 1:
        if sequence[k-1] >= sequence[k+1]:
            return k-1
    for i in range(k+1, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = first_bad_element(sequence, -1)
    if j == -1:
        return True
    if first_bad_element(sequence, j) == -1:
        return True
    if first_bad_element(sequence, j+1) == -1:
        return True
    return False

# https://newbedev.com/solve-almostincreasingsequence-codefights