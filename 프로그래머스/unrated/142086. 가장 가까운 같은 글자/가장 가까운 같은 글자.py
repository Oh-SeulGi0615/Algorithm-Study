def solution(s):
    answer = []; [answer := answer + [-1 if s[i] not in s[:i] else len(s[:i][::-1][0:s[:i][::-1].index(s[i])+1])] for i in range(len(s))]
    return answer