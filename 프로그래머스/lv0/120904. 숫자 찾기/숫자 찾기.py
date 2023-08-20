def solution(num, k):
    answer = [int(i) for i in str(num)]
    if k in answer:
        return answer.index(k) + 1
    else:
        return -1