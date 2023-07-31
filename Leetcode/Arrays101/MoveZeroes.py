# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
import random
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nonzero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonzero], nums[i] = nums[i], nums[nonzero]
            nonzero += 1

nums = [0,0,1]
print(moveZeroes(nums))