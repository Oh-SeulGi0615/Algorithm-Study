def solution(i, j, k):
    arr = ''
    for a in range(i,j+1):
        arr += str(a)
    return arr.count(str(k))