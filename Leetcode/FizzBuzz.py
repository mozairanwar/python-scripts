# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# def fizzBuzz(n: int) -> list[str]:
#     ans = []
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             ans.append("FizzBuzz")
#             continue
#         elif i % 3 == 0:
#             ans.append("Fizz")
#             continue
#         elif i % 5 == 0:
#             ans.append("Buzz")
#             continue
#         ans.append(str(i))
#     return ans

# String concat solution
def fizzBuzz(n: int) -> list[str]:
    ans = []
    for i in range(1,n+1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if not word:
            word = str(i)
        ans.append(word)
    return ans

n =15
print(fizzBuzz(n))        