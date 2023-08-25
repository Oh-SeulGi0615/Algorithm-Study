def solution(number, limit, power):
    arr = [0 for _ in range(number+1)]

    for i in range(1, number+1):
        for j in range(i, len(arr), i):
            arr[j] += 1

    arr = arr[1:]
    answer = 0
    for k in arr:
        if k > limit:
            answer += power
        else:
            answer += k
    return answer