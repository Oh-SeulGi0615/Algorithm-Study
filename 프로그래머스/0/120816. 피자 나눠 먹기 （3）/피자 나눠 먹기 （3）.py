def solution(slice, n):
    answer = 1
    while True:
        if (answer * slice) // n >= 1:
            return answer
        answer += 1