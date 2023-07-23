def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

haystack = "sadbutsad"
needle = "but"
print(strStr(haystack, needle))