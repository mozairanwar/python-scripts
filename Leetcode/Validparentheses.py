def isValid(s: str) -> bool:
    a=[]
    if len(s)%2!=0:
            return bool(False)

    for i in s:
        if i in ['(','[','{']:
            a.append(i)
        elif i is ')' and len(a)!=0 and a[-1]=='(':
            a.pop()
        elif i is ']' and len(a)!=0 and a[-1]=='[':
            a.pop()
        elif i is '}' and len(a)!=0 and a[-1]=='{':
            a.pop()
        elif i in [')','}',']'] and len(a)!=0:
            return bool(False)
        elif i in [')','}',']'] and len(a)==0:
            return bool(False)
        

    return bool(a==[])

s="(}"

if isValid(s):
    print("Valid")
else:
    print("Invalid")