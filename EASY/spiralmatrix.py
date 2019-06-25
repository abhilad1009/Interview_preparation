"""
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

"""

def spiralprint(MAT):
    u=0
    l=0
    r=len(MAT[0])-1
    d=len(MAT)-1
    while u<=d and l<=r:
        for i in range(l,r+1):
            print(MAT[u][i])
        u+=1

        for i in range(u,d+1):
            print(MAT[i][r])
        r-=1

        for i in range(r,l-1,-1):
            print(MAT[d][i])
        d-=1

        for i in range(d,u-1,-1):
            print(MAT[i][l])
        l+=1


M = [[1,  2,  3,  4],
     [21, 22, 23, 24],
     [31, 32, 33, 34],
     [6,  7,  8,  9],
     [11, 12, 13, 14],
     [16, 17, 18, 19]]

spiralprint(M)
