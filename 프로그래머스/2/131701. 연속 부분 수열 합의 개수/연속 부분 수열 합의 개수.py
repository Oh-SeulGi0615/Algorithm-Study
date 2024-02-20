def solution(elements):
    from collections import deque

    deq = deque(elements)

    result = []
    for i in range(1, len(elements)+1):
        deq = deque(maxlen=i)

        for j in elements * 2:
            deq.append(j)
            result.append(sum(deq))

    return len(set(result))