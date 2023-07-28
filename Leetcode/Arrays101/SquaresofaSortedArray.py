# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort()
    return nums

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))