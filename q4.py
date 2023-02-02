import sys
from collections import deque
input = sys.stdin.readline

s = [int(i) for i in input().strip()]
q = deque(s)
acc = q.popleft()

while q:
    cur = s.popleft()
    if acc < 2 or cur < 2: acc += cur
    else: acc *= cur

print(acc)