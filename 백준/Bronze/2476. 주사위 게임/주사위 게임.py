import sys
input = sys.stdin.readline

n = int(input())

reward = []
for _ in range(n):
    a, b, c = map(int, input().split())

    if a != b and b != c and c != a:
        sum = max(a, b, c) * 100
        reward.append(sum)

    elif a == b and b == c and c == a:
        sum = 10000 + (a * 1000)
        reward.append(sum)
    else:
        if a == b:
            sum = 1000 + (a * 100)
            reward.append(sum)
        elif b == c:
            sum = 1000 + (b * 100)
            reward.append(sum)
        elif c == a:
            sum = 1000 + (c * 100)
            reward.append(sum)

print(max(reward))