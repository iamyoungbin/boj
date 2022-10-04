# -*- coding: utf-8 -*-
#pypy3
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
schedule = list(map(int, input().split()))

plug = {}   # �����ǰ : �ش� �����ǰ�� ���� ��� ����
sol = 0
for i in range(K):
    for j in range(i+1, K):
        if schedule[i] == schedule[j]:
            next = j
            break
    else:   # schedule ���� �ش� �����ǰ ����� ������ ������ ������ �Ҵ�, K <= 100
        next = 101

    if schedule[i] in plug.keys() or len(plug) < N: # plug ���� �̹� �����ǰ�� ���� �ִ� ��� or �÷��װ� ������ ���� ���
        pass    # �ش� �����ǰ �������� �ʱ�ȭ(�߰�)
    else:
        change = max(plug, key=plug.get)    # �÷��� ������ ���� ���߿� ���Ǵ� �����ǰ ����.
        plug.pop(change)    # �÷��׿��� ����.
        sol += 1

    plug[schedule[i]] = next

print(sol)        