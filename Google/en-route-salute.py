def solution(s):
    a=[]
    salute=0
    for i in s:
        if i is ">":
            a.append(i)
        elif i is "<" and len(a)!=0:
            for j in a:
                salute+=2
                
    return print(salute)

s="<<>><<"
solution(s)