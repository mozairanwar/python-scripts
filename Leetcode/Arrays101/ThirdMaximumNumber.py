# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

def thirdMax(nums: list[int]) -> int:
    # Removing Duplicates
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.sort()
    return nums[-3]
    
nums = [-1,2,3]
print(thirdMax(nums))