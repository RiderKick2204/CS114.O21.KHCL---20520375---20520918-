import math
def Is_Special(x):
    i = 2
    n = int(math.sqrt(x))
    while (x % (i*i) != 0 and i <= n):
        i = i + 1
    return (x > 1 and i > n)

a,b = map(int,input().split())
count = 0
for i in range(a,b):
    if Is_Special(i):
        for j in range(i+1,b+1):
            if (Is_Special(j) and math.gcd(i,j)==1):
                count = count + 1
print(count)