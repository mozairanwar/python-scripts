# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
import time

def runningSum(nums: list[int]) -> list[int]:
    s = 0
    runsum = []
    for i in range(len(nums)):
        s += nums[i]
        runsum.append(s)
    return runsum

time_start = time.perf_counter()
nums = [3,1,2,10,1]
print(runningSum(nums))
time_elapsed = (time.perf_counter() - time_start)
final_res = time_elapsed * 1000
print(final_res)