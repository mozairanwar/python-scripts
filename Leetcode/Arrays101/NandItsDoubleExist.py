# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

def checkIfExist(arr: list[int]) -> bool:
    for i in range(len(arr)):
        if arr[i] == 0:
            k = arr.count(0)
            if k > 1:
                return True
            continue
        if (arr[i] * 2 or arr[i] / 2) in arr:
            return True
    return False

arr = [-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))