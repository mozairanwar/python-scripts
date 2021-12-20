import re
def calPoints(ops) -> int:
    a=[]
    for i in range(len(ops)):
        if re.match("[-+]?\d+$",ops[i]):
            a.append(int(ops[i]))
        if ops[i] is "C":
            a.pop()
        if ops[i] is "D":
            a.append(2*a[-1])
        if ops[i] is "+":
            a.append(a[-1]+a[-2])
        
    result = sum(a)
    return result

ops=['5','-2','4','C','D','9','+','+']
calPoints(ops)