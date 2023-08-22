def solution(sizes):
    for i in sizes:
        i.sort()
    sizes.sort()

    x, y = 0, 0
    for j in sizes:
        if j[0] > x:
            x = j[0]
        if j[1] > y:
            y = j[1]
    return x * y