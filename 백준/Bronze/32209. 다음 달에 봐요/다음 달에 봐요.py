questions = 0
state = True
for _ in range(int(input())):
    event, num = map(int, input().split())

    if event == 1:
        questions += num
    elif event == 2:
        questions -= num
        if questions < 0:
            state = False
            break

if state == True:
    print('See you next month')
else:
    print('Adios')