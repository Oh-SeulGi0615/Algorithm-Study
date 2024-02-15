import sys
input = sys.stdin.readline

import heapq

heap = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, [abs(n), n])
    else:
        if len(heap) > 0:
            pop = heapq.heappop(heap)
            print(pop[1])
        else:
            print(0)