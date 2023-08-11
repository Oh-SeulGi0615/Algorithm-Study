def solution(my_string, m, c):
    arr = []
    for i in range(0,len(my_string),m):
        arr.append(my_string[i:i+m][c-1])
    answer = ''.join(arr)
    return answer