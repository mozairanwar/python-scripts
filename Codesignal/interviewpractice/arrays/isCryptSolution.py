def isCryptSolution(crypt, solution):
    zipped = []
    for x in range(len(solution)):
        zipped += zip(solution[x][0], solution[x][1])
    table0 = crypt[0].maketrans(dict(zipped))
    table1 = crypt[1].maketrans(dict(zipped))
    table2 = crypt[2].maketrans(dict(zipped))
    
    a = int(crypt[0].translate(table0))
    b = int(crypt[1].translate(table1))
    c = int(crypt[2].translate(table2))

    if a + b == c and len(crypt[0]) > 1 and len(crypt[1]) > 1 and crypt[0].translate(table0)[0] != "0" and crypt[1].translate(table1)[0] != "0" and crypt[2].translate(table2)[0] != "0":
        return True
    if a + b == c and len(crypt[0]) == 1 and len(crypt[1]) == 1:
        return True
    return False

crypt=["SEND", "MORE", "MONEY"]
solution=[
    ["O","0"], 
    ["M","1"], 
    ["Y","2"], 
    ["E","5"], 
    ["N","6"], 
    ["D","7"], 
    ["R","8"], 
    ["S","9"]
    ]