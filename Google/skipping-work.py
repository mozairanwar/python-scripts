def solution(x,y):
    if len(x) > len(y):
        z=list(set(x)-set(y))
    else:
        z=list(set(y)-set(x))
    return z[0]

x=[13, 5, 6, 2, 5]
y=[5, 2, 5, 13]
solution(x,y)