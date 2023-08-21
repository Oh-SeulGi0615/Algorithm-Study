def solution(numbers, k):
    i = 0
    answer = 0
    while True:
        if k == 0:
            break

        if i % 2 == 0:
            answer = numbers[0]
            i += 1
            k -= 1
        else:
            i += 1

        numbers.append(numbers[0])
        numbers.pop(0)
    return answer