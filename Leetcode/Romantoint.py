import re
def romanToInt(s: str) -> int:
        a=[]
        re.findall("I[VX]|X[LC]|C[DM]",s)
        """ for i in s:
            if i is "I":
                if s[i+1] is "V":
                    a.append(4)
                elif s[i+1] is "X":
                    a.append(9)
                else:
                    a.append(1)
            if i is "V":
                a.append(5)
            if i is "X":
                a.append(10)
            if i is "L":
                a.append(50)
            if i is "C":
                a.append(100)
            if i is "D":
                a.append(500)
            if i is "M":
                a.append(1000) """
            
        return sum(a)

s="MCMXCIV"
romanToInt(s)