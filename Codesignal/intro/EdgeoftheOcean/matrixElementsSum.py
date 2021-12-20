import numpy as np
def matrixElementsSum(matrix):
    A = np.array(matrix)
    room = 0
    for col in range(A.shape[1]):
        for row in range(A.shape[0]):
            if A[row,col] == 0:
                break
            else:
                room += A[row,col]
    return room


matrix = [[0,1,1,2], 
    [0,5,0,0], 
    [2,0,3,3]]

matrixElementsSum(matrix)