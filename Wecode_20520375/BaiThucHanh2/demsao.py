import sys

def count_stars(image,m,n):
  count = 0
  for i in range(m):
    for j in range(n):
        if image[i][j] == '-':
            count += 1
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                if image[x][y] == '-':
                    image[x][y] = '#'
                    if x > 0 and image[x-1][y] == '-':
                        queue.append((x-1, y))
                    if x < m-1 and image[x+1][y] == '-':
                        queue.append((x+1, y))
                    if y > 0 and image[x][y-1] == '-':
                        queue.append((x, y-1))
                    if y < n-1 and image[x][y+1] == '-':
                        queue.append((x, y+1))

  return count

Case = 1
eof = False
while not eof:
    line = sys.stdin.readline()
    if line == "":
        eof = True
    else:
        image = []
        m,n = map(int,line.strip().split())
        for _ in range(m):
            image.append(list(input().strip()))
        count = count_stars(image,m,n)
        print('Case {}: {}'.format(Case,count))
        Case = Case + 1
        Count = 0