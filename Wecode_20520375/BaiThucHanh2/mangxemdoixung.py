import sys

n = (int)(input())
input = sys.stdin.read()
L = input.strip().split()
count = 0
check = True
for i in range((int)(n/2)):
    if (L[i] != L[n-i-1]):
        count = count + 1
        if (count > 1):
            check = False
            break
print(str(check).upper())