def solution(citations):
    matrix = [[0 for _ in range(10000)] for _ in range(10000)]
    cit = sorted(citations, key=lambda x: -x)

    for i in range(len(cit)):
        for j in range(cit[i]):
            matrix[i][j] = 1

    h_index = 0
    for k in range(0, 10000):
        if matrix[k][k] == 1:
            h_index += 1
        else:
            break
    return h_index