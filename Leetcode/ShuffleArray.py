def shuffle(nums: list[int], n: int) -> list[int]:
    x = nums[:n]
    y = nums[n::]
    z = []
    for i in range(n):
        z.append(x[i])
        z.append(y[i])
    return z

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))