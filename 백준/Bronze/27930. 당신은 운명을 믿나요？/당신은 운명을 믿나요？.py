import sys
input = sys.stdin.readline

a = list(input().rstrip())

list1, list2 = ['K','O','R','E','A'], ['Y','O','N','S','E','I']
cnt1, cnt2 = 0, 0

for i in range(len(a)):
    if a[i] == list1[cnt1] or a[i] == list2[cnt2]:
        if a[i] == list1[cnt1]:
            cnt1 += 1
        elif a[i] == list2[cnt2]:
            cnt2 += 1

    if cnt1 == len(list1) or cnt2 == len(list2):
        if cnt1 == len(list1):
            print('KOREA')
            break
        elif cnt2 == len(list2):
            print('YONSEI')
            break