import sys
import heapq

def command(heap, q):
    if (heap):
        if (q[0] == -1):
                heapq.heappop(heap)
        if (q[0] == -2):
            m = heap[0]
            while (heap and heap[0] == m):
                heapq.heappop(heap)
        if (q[0] == -3):
            m = heap[0] + q[1]
            heapq.heappushpop(heap,m)
        if (q[0] == -4):
            m = heap[0]
            while (heap and heap[0] == m):
                    heapq.heappushpop(heap,m + q[1])
    return

# n,m = map(int,input().split())
# H = []
# for i in range(n):
#     x = int(input())
#     heapq.heappush(H,-x)
# for i in range(m):
#     x = list(map(int,input().split()))
#     command(H,x)
# while H:
#     print(-H[0])
#     heapq.heappop(H)

n,m = map(int,sys.stdin.readline().split())
H = []
for i in range(n):
    input = sys.stdin.readline().strip()
    H.append(-int(input))
heapq.heapify(H)
for j in range(m):
    input = list(map(int,sys.stdin.readline().strip().split()))
    command(H,input)
sorted_arr = "\n".join(str(-heapq.heappop(H)) for i in range(len(H)))
print(sorted_arr)