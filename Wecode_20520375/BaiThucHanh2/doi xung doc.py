a,b = map(int,input().split())
L = []
for i in range(a):
    x = list(map(int,input().split()[:b]))
    L.append(x)

for i in range(a):
    for j in range(b):
        print(L[a-i-1][j],end=' ')
    print()