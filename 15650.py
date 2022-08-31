# -*- coding: utf-8 -*-
N, M = map(int, input().split())
list = [0 for _ in range(M)]

def promising(index):
    if N-list[index] >= M-1-index:  ## 사용가능한 숫자 수 >= 채워야 할 남은 자리 수
        return True
    else:
        return False

def solve(index):
    if index == M:  # index가 리스트를 초과하면, 리스트가 꽉 차면 출력
        print(*list)
        return

    for i in range(1, N+1):
        if index == 0:  # list의 첫번째 원소면 그냥 넣음
            list[index] = i
            if promising(index):
                solve(index+1)
        elif i > list[index-1]: # list의 두번째 원소부터는 그 전 원소보다 큰 원소만 추가될 수 있음
            list[index] = i
            if promising(index):
                solve(index+1)

solve(0)