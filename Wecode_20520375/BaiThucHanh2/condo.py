a,b = map(int,input().split())

L = []

for i in range(b):
    x,y = input().split(' ')
    x = int(x)
    L.append([x,y])
count = 0
T = 0
a = a * 100
pos = 'right'
old_pos = ''
for i in range(b):
    x,y = L[i]
    if (y != pos):
        count = count + 1
        pos = y
        T = x
    else:
        if (T + x <= a):
            T = T + x
        else:
            if (old_pos == pos):
                count = count + 2
            else:
                count = count + 1
            T = x
    old_pos = pos
if (y == pos and pos == 'right'):
    if (T + x > a):
        if (old_pos == pos):
            count = count + 2
print(count)