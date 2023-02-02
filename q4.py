import sys
from collections import deque
input = sys.stdin.readline

arr = [int(i) for i in input().strip()]
q = deque(arr)
acc = q.popleft()

while q:
    cur = q.popleft()
    if acc < 2 or cur < 2: acc += cur
    else: acc *= cur

print(acc)