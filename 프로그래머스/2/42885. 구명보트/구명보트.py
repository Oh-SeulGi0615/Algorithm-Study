def solution(people, limit):
    from collections import deque

    people = deque(sorted(people))

    cnt = 0
    while people:
        if len(people) == 1:
            cnt += 1
            people.pop()

        elif people[0] + people[-1] <= limit:
            cnt += 1
            people.popleft()
            people.pop()

        else:
            cnt += 1
            people.pop()

    return cnt