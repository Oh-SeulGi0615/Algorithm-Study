def solution(intStrs, k, s, l):
    arr = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            arr.append(int(i[s:s+l]))
    return arr