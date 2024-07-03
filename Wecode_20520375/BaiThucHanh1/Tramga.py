a,b = input()
c,d = input()
a = ord(a)
b = ord(b)
c = ord(c)
d = ord(d)

if (a & b & c & d == 35):
    print('Yes')
else:
    case_1 = (a & b) | (a & d) | (d & c) | (b & c)
    case_2 = (((a==c) and (a==35)) or ((b==d) and (b==35))) 
    if (case_1 & 35 == 35 or case_2):
        if (a != d or b != c):
            print('Yes')
        else:
            print('No') 
    else:
        print('No')