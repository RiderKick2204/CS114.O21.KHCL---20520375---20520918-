n = int(input())
L = []
for i in range(n):
    x = int(input())
    L.append(x)
L.sort()
count = 0
for i in range(1,n):
    count = count + L[i] - L[i-1] - 1
print(count)