import sys
input = sys.stdin.readline

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

import datetime

date1 = datetime.datetime(y1, m1, d1)
date2 = datetime.datetime(y2, m2, d2)

diff = date2 - date1

if diff.days > 365242:
    print('gg')
else:
    print(f'D-{diff.days}')