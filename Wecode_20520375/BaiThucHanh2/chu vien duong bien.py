a,b = map(int,input().split())
L = [[0](b+2)]
for i in range(a)
    x = list(map(int,input().split()[b]))
    x = [0] + x + [0]
    L.append(x)
L.append([0](b+2))

S = 0
for i in range(1,a+1)
    for j in range(1,b+1)
        sub_S = 4
        if (L[i][j] == 1)
            if (L[i][j-1]==1)
                sub_S = sub_S - 1
            if (L[i-1][j]==1)
                sub_S = sub_S - 1
            if (L[i][j+1]==1)
                sub_S = sub_S - 1
            if (L[i+1][j]==1)
                sub_S = sub_S - 1
        else
            sub_S = 0
        S = S + sub_S 
print(S)