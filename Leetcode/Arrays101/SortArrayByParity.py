# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

def sortArrayByParity(nums: list[int]) -> list[int]:
    odd = 0
    for even in range(len(nums)):
        if nums[even] % 2 == 0:
            nums[even], nums[odd] = nums[odd], nums[even]
            odd += 1
    return nums

nums = [1]
print(sortArrayByParity(nums))