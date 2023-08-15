def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for j in range(len(arr)):
            if j % 2 == 1:
                answer.append(arr[j] + n)
            else:
                answer.append(arr[j])
    return answer