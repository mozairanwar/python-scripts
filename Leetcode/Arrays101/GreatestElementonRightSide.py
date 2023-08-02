# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

def replaceElements(arr: list[int]) -> list[int]:
    val = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > val:
            arr[i], val = val, arr[i]
        else:
            arr[i] = val
    arr[-1] = -1
    return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))