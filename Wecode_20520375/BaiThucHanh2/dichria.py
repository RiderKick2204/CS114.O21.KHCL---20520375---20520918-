from collections import deque
import random as rd

def rotateLeft(arr):
    arr.append(arr[0])
    arr.popleft()
    return arr

def rotateRight(arr):
    arr.appendleft(arr[-1])
    arr.pop()
    return arr

def flat(matrix,x,row,col):
    T = deque()
    if (row-x-1==x):
        for i in range(x,col-x):
            T.append(matrix[x][i])
        return T
    if (col-x-1==x):
        for i in range(x,row-x):
            T.append(matrix[i][col-x-1])
        return T
    
    for i in range(x,col-x):
        T.append(matrix[x][i])
    for i in range(x+1,row-x):
        T.append(matrix[i][col-x-1])
    for i in range(x+1,col-x):
        T.append(matrix[row-x-1][col-i-1])
    for i in range(x+1,row-x-1):
        T.append(matrix[row-i-1][x])
    return T

def rotate_border_x(border,matrix,x,row,col):

    k = 0 
    if (row-x-1==x):
        for i in range(x,col-x):
            matrix[x][i] = border[k]
            k = k + 1
        return matrix
    if (col-x-1==x):
        for i in range(x,row-x):
            matrix[i][col-x-1] = border[k]
            k = k + 1
        return matrix
    

    for i in range(x,col-x):
        matrix[x][i] = border[k]
        k = k + 1
    for i in range(x+1,row-x):
        matrix[i][col-x-1] = border[k]
        k = k + 1
    for i in range(x+1,col-x):
        matrix[row-x-1][col-i-1] = border[k]
        k = k + 1
    for i in range(x+1,row-x-1):
        matrix[row-i-1][x] = border[k]
        k = k + 1
    return matrix

def IN(matrix):
    for row in matrix:
        for num in row:
            print(num,end=' ')
        print()

r, c = map(int, input().split())
L = []
for i in range(r):
    L.append(list(map(int,input().split())))
k = 0
odd = False 
if (r == c):
    k = (r//2) + (r%2)
else:
    M = min(r,c)
    k = (M//2) + (M%2)

for i in range(k):
    T = flat(L,i,r,c)
    if (i%2 != 0):
        T = rotateLeft(T)
    else:
        T = rotateRight(T)
    L = rotate_border_x(T,L,i,r,c)
IN(L)