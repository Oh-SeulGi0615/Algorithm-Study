def solution(my_strings, parts):
    arr = []
    for i in range(len(parts)):
        a = my_strings[i][parts[i][0]:parts[i][1]+1]
        arr.append(a)
    answer = ''.join(arr)
    return answer