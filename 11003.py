import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

dq = deque()
for i in range(N):
    while dq and dq[-1] > number[i]:
        dq.pop()
    dq.append(number[i])

    if i-L >= 0 and dq[0] == number[i-L]:
        dq.popleft()

    print(dq[0], end=" ")