# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

def duplicateZeros(arr: list[int]) -> None:
    index = 0
    for i in range(len(arr)):
        if index < len(arr) and arr[index] == 0:
            arr.pop()
            arr.insert(index, 0)
            index += 2
            continue
        
        index += 1
    print(arr)


arr = [0,4,1,0,0,8,0,0,3]
print(duplicateZeros(arr))