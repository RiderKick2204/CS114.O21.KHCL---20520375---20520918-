def vector(a,b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return [x,y]

def Is_RightTurn(x,y):
    if (x==[-1,0] and y == [0,1]):
        return True
    if (x==[1,0] and y == [0,-1]):
        return True
    if (x==[0,1] and y == [1,0]):
        return True
    if (x==[0,-1] and y == [-1,0]):
        return True
    return False

a = int(input())
L = []
for i in range(a):
    x,y = input().split()
    L.append([int(x),int(y)])

count = 0
vect = []
for i in range(1,a):
    x = vector(L[i-1],L[i])
    vect.append(x)
for i in range(len(vect) - 1):
    if (Is_RightTurn(vect[i],vect[i+1])):
        count = count + 1
print(count)