def commonCharacterCount(s1, s2):
    ccc=0
    if len(s1) < len(s2):
        for i in s1:
            if i in s2:
                s1=s1.replace(i,'',1)
                s2=s2.replace(i,'',1)
                ccc+=1
    else:
        for i in s2:
            if i in s1:
                s1=s1.replace(i,'',1)
                s2=s2.replace(i,'',1)
                ccc+=1
    return ccc
