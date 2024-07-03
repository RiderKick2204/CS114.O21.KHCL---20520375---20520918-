def binary_search(x,arr):
  L = 0
  R = len(arr) - 1
  while (L <= R):
    mid = (L + R) // 2
    if (arr[mid] == x): 
      return True
    if (arr[mid] > x):
      R = mid - 1
    else:
      L = mid + 1
  return False
 
m,n = map(int,input().split())
sys_user = list(map(int,input().split()[:m]))
friend = list(map(int,input().split()[:n]))
count = 0
for x in friend:
    if (binary_search(x,sys_user)):
      count = count + 1
print(count)