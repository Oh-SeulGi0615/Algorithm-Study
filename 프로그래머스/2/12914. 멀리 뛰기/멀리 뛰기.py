def solution(n):
    arr = [1, 2]

    if n == 1: result = 1
    elif n == 2: result = 2
    else:
        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])
        result = arr[-1]
    
    return result % 1234567