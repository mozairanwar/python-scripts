# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxones = 0
    ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ones += 1
        else:
            if ones > maxones:
                maxones = ones
            ones = 0
    if ones > maxones:
        maxones = ones
    return maxones

nums = [1,1,1,1,1,1]
print(findMaxConsecutiveOnes(nums))