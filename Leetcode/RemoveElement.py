def removeElement(nums: list[int], val: int) -> int:
    for i in range(len(nums)-1,-1,-1):
        print(i, nums[i])
        if nums[i] == val:
            nums.remove(nums[i])
    k = len(nums)
    return k, nums

nums = [1]
val = 1
print(removeElement(nums, val))