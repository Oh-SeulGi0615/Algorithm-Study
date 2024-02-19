def solution(n,a,b):
    cnt = 1
    group_a = (a // 2) + (a % 2)
    group_b = (b // 2) + (b % 2)

    while True:
        if group_a == group_b:
            break

        cnt += 1
        group_a = (group_a // 2) + (group_a % 2)
        group_b = (group_b // 2) + (group_b % 2)

    return cnt