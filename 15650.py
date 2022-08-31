# -*- coding: utf-8 -*-
N, M = map(int, input().split())
list = [0 for _ in range(M)]

def promising(index):
    if N-list[index] >= M-1-index:  ## ��밡���� ���� �� >= ä���� �� ���� �ڸ� ��
        return True
    else:
        return False

def solve(index):
    if index == M:  # index�� ����Ʈ�� �ʰ��ϸ�, ����Ʈ�� �� ���� ���
        print(*list)
        return

    for i in range(1, N+1):
        if index == 0:  # list�� ù��° ���Ҹ� �׳� ����
            list[index] = i
            if promising(index):
                solve(index+1)
        elif i > list[index-1]: # list�� �ι�° ���Һ��ʹ� �� �� ���Һ��� ū ���Ҹ� �߰��� �� ����
            list[index] = i
            if promising(index):
                solve(index+1)

solve(0)