def solution(k, score):
    result, answer = [], []
    for i in score:
        result.append(i)
        result.sort()
        answer.append(result[::-1][:k][-1])
    return answer