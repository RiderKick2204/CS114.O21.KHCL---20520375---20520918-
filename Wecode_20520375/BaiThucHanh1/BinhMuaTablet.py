import math
import time
diagonal = int(input())
square_diagonal = diagonal**2
stop = int(diagonal/math.sqrt(2))
start = int(diagonal/2)
count = 0

for wide in range(stop,diagonal):
    long = math.sqrt(square_diagonal - wide**2)
    if (long.is_integer()):
        count += 1
print(count)