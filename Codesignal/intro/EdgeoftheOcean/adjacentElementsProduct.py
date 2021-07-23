def adjacentElementsProduct(inputArray):
    x=[]
    for i in range(len(inputArray)-1):
        x.append(inputArray[i]*(inputArray[i+1]))
    return max(x)
