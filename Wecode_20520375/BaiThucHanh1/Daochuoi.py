def reverse(b):
    res = ''
    for x in b:
        res = x + res
    return res
n = int(input())
for i in range(n):
    a = input()
    b = input()
    check = (a.find(b) > -1 or a.find(reverse(b)) > -1)
    if (check):
        print('YES')
    else:
        print('NO')