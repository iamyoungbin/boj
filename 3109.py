# -*- coding: utf-8 -*-
import sys
from collections import deque

def dfs(y, x):
    stack = deque()
    stack.append((y, x))
    
    while stack:
        cur_y, cur_x = stack.pop()
        visited[cur_y][cur_x] = True
        if cur_x == C-1:
            return 1
        
        for i in range(3):  # dfs�� �밢�� ��, ������, �밢�� �Ʒ� ������ Ž���ϵ��� ��.
            # ���� ��ܿ������� Ž���� ������ �� ������������ �ִ��� ������� �ٴ� ���� �� ������������ �����ϴ� ������ �������Ƿ�.
            next_y, next_x = cur_y+dy[i], cur_x+1
            if 0 <= next_y < R and world[next_y][next_x] == '.' and visited[next_y][next_x] == False:
                stack.append((next_y, next_x))
            
    return 0
        
input = sys.stdin.readline

R, C = map(int, input().split())
world = [input().rstrip() for _ in range(R)]
    
visited = [[False for _ in range(C)] for _ in range(R)]
dy = [1, 0, -1]
sol = 0

for i in range(R):
    sol += dfs(i, 0)
    
print(sol)