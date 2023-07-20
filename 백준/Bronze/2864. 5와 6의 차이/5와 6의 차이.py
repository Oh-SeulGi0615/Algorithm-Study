import sys
input = sys.stdin.readline
import re

a, b = map(str, input().split())

low = int(re.sub('6', '5', a)) + int(re.sub('6', '5', b))
high = int(re.sub('5', '6', a)) + int(re.sub('5', '6', b))

print(low, high)