import sys
input = sys.stdin.readline

r = int(input())
list1 = list(input().rstrip())

n = int(input())

score = 0
list2 = []
for _ in range(n):
    arr = list(input().rstrip())
    list2.append(arr)

    for i in range(r):
        if list1[i] == 'S':
            if arr[i] == 'S':
                score += 1
            elif arr[i] == 'P':
                score += 2
            else:
                pass
        elif list1[i] == 'P':
            if arr[i] == 'P':
                score += 1
            elif arr[i] == 'R':
                score += 2
            else:
                pass
        elif list1[i] == 'R':
            if arr[i] == 'R':
                score += 1
            elif arr[i] == 'S':
                score += 2
            else:
                pass

print(score)

top = 0
for i in range(r):
    arr = {'S':0, 'P':0, 'R':0}
    for j in range(n):
        arr[list2[j][i]] += 1
    top += max(arr['S'] * 2 + arr['R'], arr['P'] * 2 + arr['S'], arr['R'] * 2 + arr['P'])

print(top)