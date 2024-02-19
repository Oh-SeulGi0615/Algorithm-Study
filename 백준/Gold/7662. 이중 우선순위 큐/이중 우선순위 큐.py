import sys
input = sys.stdin.readline

import heapq

def pop(heap):
    while len(heap) > 0:
        data, idx = heapq.heappop(heap)
        if not deleted[idx]:
            deleted[idx] = True
            return data
    return None

for _ in range(int(input())):
    min_heap, max_heap = [], []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    n = int(input())
    current = 0
    deleted = [False] * (n + 1)

    for _ in range(n):
        list_ = input().split()
        order, number = list_[0], int(list_[1])

        if order == 'I':
            heapq.heappush(min_heap, (number, current))
            heapq.heappush(max_heap, (-number, current))
            current += 1
        
        elif order == 'D':
            if number == 1:
                pop(max_heap)
            elif number == -1:
                pop(min_heap)

    max_value = pop(max_heap)
    if max_value == None:
        print('EMPTY')
    else:
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))