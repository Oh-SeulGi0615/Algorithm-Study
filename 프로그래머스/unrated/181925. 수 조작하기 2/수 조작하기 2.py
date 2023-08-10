def solution(numLog):
    arr = []
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            arr.append('w')
        elif numLog[i+1] - numLog[i] == -1:
            arr.append('s')
        elif numLog[i+1] - numLog[i] == 10:
            arr.append('d')
        elif numLog[i+1] - numLog[i] == -10:
            arr.append('a')
    result = ''.join(arr)
    return result