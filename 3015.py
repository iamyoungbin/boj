# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

stack = deque()
N = int(input())
sol = 0
for i in range(N):
    high = int(input())
    cnt = 0
    same = 0
    while stack:    # high에 따른 내림차순 정렬
        if stack[len(stack)-1][0] > high:   # peek(stack) > high, 루프문 종료
            cnt += 1
            break

        temphigh, tempsame = stack.pop()
        if temphigh == high:
            same = tempsame+1

        cnt += tempsame + 1

    sol += cnt # n번째 high와 1~n-1 번째 high 사이의 순서쌍 갯수 더하기.
    stack.append((high, same))  # (높이, 순차적으로 이어진 동일 high의 개수-1)
    # print(*stack, "{}(+{})".format(sol, cnt+same))
    
print(sol)