import sys
input = sys.stdin.readline

x_list, y_list = [], []
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in x_list:
        x_list.append(x)
    if y not in y_list:
        y_list.append(y)

answer = 2*(max(x_list) - min(x_list)) + 2*(max(y_list) - min(y_list))
print(answer)