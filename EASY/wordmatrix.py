"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

"""


def search(i,j,word,wl,r,c):
    global mat
    if i>=r or j>=c:
        return False
    
    colword,rowword=None,None
    if i+wl<=r and j<=c:
        colword=""
        for _ in range(wl):
            colword+=mat[i+_][j]
    if j+wl<=c and i<=r:
        rowword="".join(mat[i][j:j+wl])
    
    if rowword==word or colword==word:
        return True

    rowrecursion=search(i,j+1,word,wl,r,c) if colword else None
    colrecursion=search(i+1,j,word,wl,r,c) if rowword else None

    return rowrecursion or colrecursion

def check(word,matrix):
    return search(0,0,word,len(word),len(matrix),len(matrix[0]))

mat = [['F', 'A', 'C', 'I'],
       ['O', 'B', 'Q', 'P'],
       ['A', 'N', 'O', 'B'],
       ['M', 'A', 'S', 'S']]

print(check("MASS",mat))