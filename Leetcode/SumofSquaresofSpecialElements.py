# You are given a 1-indexed integer array nums of length n.
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
# Return the sum of the squares of all special elements of nums.
import time
# import resource
def sumOfSquares(nums: list[int]) -> int:
    n = len(nums)
    k = 0
    for i in range(1,len(nums)+1):
        if n % i == 0:
            k = k + nums[i-1]*nums[i-1]
    return k

time_start = time.perf_counter()
nums = [2,7,1,19,18,3]
sumOfSquares(nums)
time_elapsed = (time.perf_counter() - time_start)
print(time_elapsed)