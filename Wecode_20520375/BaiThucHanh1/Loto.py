res = [[0,0,0],[0,0,0],[0,0,0]]
L = []
for i in range(3):
  Col = [int(x) for x in input().split()]
  L.append(Col)

n = int(input())
for i in range(n):
  x = int(input())
  for i in range(3):
    for j in range(3):
      if (x == L[i][j]):
        res[i][j] = 1

def check_ticket(res):
  if (res[0][0]+res[1][1]+res[2][2]==3):
    return True
  if (res[0][2]+res[1][1]+res[2][0]==3):
    return True
  for i in range(3):
    if (res[i][0] + res[i][1]+ res[i][2]==3):
      return True
    if (res[0][i] + res[1][i]+ res[2][i]==3):
      return True

if (check_ticket(res)):
  print('Yes') 
else:
  print('No')