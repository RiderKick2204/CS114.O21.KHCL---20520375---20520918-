a,b = map(int,input().split())
L = []
for x in range(a):
    L.append(list(map(int,input().split(' ')[:b])))
    
max_widths = []
for i in range(b):
    max_width = len(str(L[0][i]))
    for j in range(1,a):
        max_width = max(max_width,len(str(L[j][i])))
    max_widths.append(max_width)

for row in L:
    for i, value in enumerate(row):
        print(f"{value:>{max_widths[i]}} ", end="")
    print()