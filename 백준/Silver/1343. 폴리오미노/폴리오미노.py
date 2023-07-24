import sys
input = sys.stdin.readline
import re

n = input().rstrip()

n = re.sub('XXXX', 'AAAA', n)
n = re.sub('XX', 'BB', n)

if 'X' in n:
    print(-1)
else:
    print(n)