#Nhap 
m = int(input())
arr_m = list(map(int,input().split()[:m]))
n = int(input())
arr_n = list(map(int,input().split()[:n]))

#Xu ly
pos = {}
for i in range(m):
  pos[arr_m[i]] = i 
for x in arr_n:
  if (x in pos):
    print(pos[x])
  else:
    print(-1)