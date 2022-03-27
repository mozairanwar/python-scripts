import re
def romanToInt(s: str) -> int:
        romdict={
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
            }
        value=0
        for i in range(len(s)):
            if i+1 < len(s) and romdict[s[i]] < romdict[s[i+1]]:
                value-=romdict[s[i]]
            else:
                value+=romdict[s[i]]
        
        return value
        # a=re.findall("I[VX]|X[LC]|C[DM]|I|V|X|L|C|D|M",s)
        # b=re.findall("I[VX]|X[LC]|C[DM]", s)
        # g=[]
        # for i in a[:]:
        #     if i in b:
        #         a.remove(i)
        # romdict={
        #         "I":'1',
        #         "V":'5',
        #         "X":'10',
        #         "L":'50',
        #         "C":'100',
        #         "D":'500',
        #         "M":'1000'
        #     }
        
        # for i in a:
        #     z=i.maketrans(romdict)
        #     g.append(int(i.translate(z)))

        # for i in b:
        #     if i == "IV":
        #         g.append(4)
        #     if i == "IX":
        #         g.append(9)
        #     if i == "XL":
        #         g.append(40)
        #     if i == "XC":
        #         g.append(90)
        #     if i == "CD":
        #         g.append(400)
        #     if i == "CM":
        #         g.append(900)
        
        # return value(g)

s="MCMXCIV"
print(romanToInt(s))