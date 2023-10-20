def solution(n):
    cnt = 1
    sum_ = 0
    start = 1
    while True:
        if start > n:
            break
        for i in range(start, n):
            sum_ += i
            if sum_ == n:
                cnt += 1
            elif sum_ > n:
                break
        start += 1
        sum_ = 0
    return cnt
        