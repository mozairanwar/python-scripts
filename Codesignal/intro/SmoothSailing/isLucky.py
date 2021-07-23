def isLucky(n):
    stn = str(n)
    lin = list(stn)
    a=0
    b=0
    for i in range(len(stn)//2): # Floor division to avoid float
        a += (int(lin[i]))
    for i in range(1, len(stn)//2+1):
        b += (int(lin[-i]))
    return a == b
