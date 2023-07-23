def removeDuplicates(nums: list[int]) -> int:
    l=1
    for i in range(len(nums)):
        if i != 0 and nums[i] != nums[i-1]:
            nums[l] = nums[i]
            l += 1
    return l

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))