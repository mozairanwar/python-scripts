# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

from typing import Counter
# def canConstruct(ransomNote: str, magazine: str) -> bool:
#     if len(magazine) < len(ransomNote):
#         return False
#     test = {}
#     for i in magazine:
#         if not test.get(i):
#             test[i] = magazine.count(i)

#     for j in ransomNote:
#         if not test.get(j):
#             return False
#         if test.get(j) < ransomNote.count(j):
#             return False
#     return True

# Alternate Solution
def canConstruct(ransomNote: str, magazine: str) -> bool:
    note, mag = Counter(ransomNote), Counter(magazine)
    if note & mag == note:
        return True
    return False

ransomNote = "aab"
magazine = "baa"
print(canConstruct(ransomNote, magazine))