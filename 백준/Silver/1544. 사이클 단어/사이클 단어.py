import sys
input = sys.stdin.readline

from collections import deque

string_set = []
cnt = 0
for _ in range(int(input())):
    string = input().rstrip()

    if string not in string_set:
        string_deque = deque(list(string))

        for _ in range(len(string)):
            result = ''.join(string_deque)
            string_set.append(result)
            string_deque.rotate(-1)

        cnt += 1

print(cnt)