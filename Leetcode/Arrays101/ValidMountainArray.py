# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def validMountainArray(arr: list[int]) -> bool:
    if len(arr) < 3:
        return False
    
    peak = -1
    # Ascend to peak
    for i in range(len(arr)):
        if peak < arr[i]:
            peak = arr[i]
        elif peak > arr[i]:
            break
        else:
            return False

    ipeak = i-1
    if ipeak == len(arr)-1 or ipeak == 0:
        return False
    arr = arr[ipeak:]

    # Descend from peak
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            continue
        else:
            return False

    return True

arr = [4,3,2,1]
print(validMountainArray(arr))