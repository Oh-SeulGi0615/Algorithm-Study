t = int(input())

for _ in range(t):
    num = int(input())

    answer = 0
    for i in range(2, 65):
        result = []
        num_ = num
        while num_:
            result.append([num_ % i])
            num_ //= i

        if result == result[::-1]:
            answer = 1
    print(answer)