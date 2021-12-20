import re
def isValid(s: str) -> bool:
    a=[]
    for i in s:
        if i in ['(','[','{']:
            a.append(i)
        elif i is ')' and len(a)!=0 and a[-1]=='(':
            a.pop()
        elif i is ']' and len(a)!=0 and a[-1]=='[':
            a.pop()
        elif i is '}' and len(a)!=0 and a[-1]=='{':
            a.pop()

    return bool(a==[])

s="()]{}"

if isValid(s):
    print("Valid")
else:
    print("Invalid")