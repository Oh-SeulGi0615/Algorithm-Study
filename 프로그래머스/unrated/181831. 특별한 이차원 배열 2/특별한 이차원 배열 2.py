def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer.append(True)
            else:
                answer.append(False)

    if False in answer:
        return 0
    else:
        return 1