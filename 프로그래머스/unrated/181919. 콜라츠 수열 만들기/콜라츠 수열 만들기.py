def solution(n):
    arr = [n]
    while n > 1:
        if n % 2 == 0:
            arr.append(int(n / 2))
            n = int(n / 2)
        else:
            arr.append((3 * n) + 1)
            n = 3*n + 1

    return arr