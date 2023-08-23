def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    answer2 = ''
    for i in range(1, len(food)):
        answer2 += str(i) * (food[i] // 2)
    return answer + '0' + answer2[::-1]