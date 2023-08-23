def solution(n, arr1, arr2):
    base = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(arr1)):
        binary1 = str(bin(arr1[i])[2:]).zfill(n)
        binary2 = str(bin(arr2[i])[2:]).zfill(n)

        for j in range(len(binary1)):
            if binary1[j] == '1' or binary2[j] == '1':
                base[i][j] = 1

    answer = []
    for k in base:
        base_string = ''
        for l in k:
            if l == 1:
                base_string += '#'
            else:
                base_string += ' '
        answer.append(base_string)
    return answer