# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits: list[int]) -> list[int]:
    num=""
    for i in range(len(digits)):
        num += str(digits[i])
    num = str(int(num) + 1)
    digits.clear()
    for j in range(len(num)):
        digits.append(int(num[j]))
    return digits

digits = [1,2,3]
print(plusOne(digits))