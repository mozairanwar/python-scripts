def ruler(case_num):
    kingdom = input()
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if kingdom[-1] in vowels:
        print(f"Case #{case_num}: {kingdom} is ruled by Alice.")
    elif kingdom[-1] in ["Y", "y"]:
        print(f"Case #{case_num}: {kingdom} is ruled by nobody.")
    else:
        print(f"Case #{case_num}: {kingdom} is ruled by Bob.")

num_cases= int(input())
for i in range(num_cases):
    ruler(i+1)