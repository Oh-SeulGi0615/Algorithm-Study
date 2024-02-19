def solution(n, words):
    from collections import deque

    person = deque([i for i in range(1, n+1)])
    word_list = []
    check = [False] * n
    cnt = 0

    for i in range(len(words)):
        cnt = (i // n) + 1
        
        if not word_list:
            word_list.append(words[i])
            person.rotate(-1)

        elif words[i] in word_list or words[i][0] != word_list[-1][-1]:
            return [person[0], cnt]

        else:
            word_list.append(words[i])
            person.rotate(-1)
    return [0, 0]