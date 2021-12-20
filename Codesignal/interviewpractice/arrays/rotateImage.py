import numpy
def rotateImage(a):
    a = numpy.transpose(a)
    for i in range(len(a)):
        for j in range(len(a)//2):
            a[i][j], a[i][-j-1]  = a[i][-j-1], a[i][j]
    return a