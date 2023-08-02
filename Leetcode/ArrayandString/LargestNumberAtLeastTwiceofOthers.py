# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

def dominantIndex(nums: list[int]) -> int:
    index = nums.index(max(nums))
    for i in nums:
        if i > nums[index]/2 and i != nums[index]:
            return -1
    return index

nums = [3,6,1,0]
print(dominantIndex(nums))