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
    while stack:    # high�� ���� �������� ����
        if stack[len(stack)-1][0] > high:   # peek(stack) > high, ������ ����
            cnt += 1
            break

        temphigh, tempsame = stack.pop()
        if temphigh == high:
            same = tempsame+1

        cnt += tempsame + 1

    sol += cnt # n��° high�� 1~n-1 ��° high ������ ������ ���� ���ϱ�.
    stack.append((high, same))  # (����, ���������� �̾��� ���� high�� ����-1)
    # print(*stack, "{}(+{})".format(sol, cnt+same))
    
print(sol)