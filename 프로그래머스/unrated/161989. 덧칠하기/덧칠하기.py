def solution(n, m, section):
    count = 0
    paint = section[0]-1
    for i in section:
        if i > paint:
            paint = i+m-1
            count += 1
    return count