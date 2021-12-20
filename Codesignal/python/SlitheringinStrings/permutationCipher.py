def permutationCipher(password, key):
    table = password.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    print(table)
    return password.translate(table)

password = "iamthebest"
key = "zabcdefghijklmnopqrstuvwxy"
permutationCipher(password, key)