from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        cp=[]
        for i in strs[0]:
            cp.append(i)
        l=[]
        
        for i in strs:
            l.append(len(i))
        del cp[min(l):]
        
        for i in range(1,len(strs)):
            for j in range(0,len(cp)):
                if strs[i][j] != cp[j]:
                    del cp[j:]
                    break
        
        lcp=""
        print(lcp.join(cp))

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)