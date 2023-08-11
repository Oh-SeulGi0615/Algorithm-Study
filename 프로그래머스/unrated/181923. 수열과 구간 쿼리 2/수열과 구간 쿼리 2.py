def solution(arr, queries):
    arr2 = []
    for i in range(len(queries)):
        arr3 = []  
        for j in range(queries[i][0], queries[i][1]+1):
            if arr[j] > queries[i][-1]:
                arr3.append(arr[j])
        if len(arr3) > 0:
            arr2.append(min(arr3))
        else:
            arr2.append(-1)
    return arr2