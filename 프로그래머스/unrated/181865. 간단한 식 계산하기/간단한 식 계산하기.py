def solution(binomial):
    arr = binomial.split()

    if arr[1] == '+':
        answer = int(arr[0]) + int(arr[-1])
    elif arr[1] == '-':
        answer = int(arr[0]) - int(arr[-1])
    else:
        answer = int(arr[0]) * int(arr[-1])
        
    return answer