def firstNotRepeatingCharacter(s):
    seen = []
    for i in s:
        if i not in seen:
            seen.append(i)
        elif i in seen:
            s = s.replace(i,"")
    return s[0] if len(s) > 0 else "_"
