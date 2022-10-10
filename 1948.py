# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m  = int(input())
edge = [[] for _ in range(n+1)]
edge_reverse = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
max_time = [-1 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((c, b))
    edge_reverse[b].append((c, a))
    degree[b] += 1
    
start, end = map(int, input().split())
dq = deque()
max_time[start] = 0
dq.append((0, start))
while dq:   # topological sort
    cur_time, cur_vertex = dq.popleft()
        
    for weight, next_vertex in edge[cur_vertex]:
        degree[next_vertex] -= 1
        if cur_time + weight > max_time[next_vertex]:   # ���� �������� ���� �ִ��� �� ������Ʈ
            max_time[next_vertex] = cur_time + weight
            
        if degree[next_vertex] == 0:    # ��� ���� ���� �� ������������ �ִ������� �����ϴ� ���� �̿�
            dq.append((max_time[next_vertex], next_vertex))

dq = deque()
dq.append((max_time[end], end))
lane = [[] for _ in range(n+1)] # ���� �̿뿡 ���� �ߺ� ��� ����
total_lane = 0
while dq:   # �����������κ��� ����������� ���������� bfs
    cur_time, cur_vertex = dq.popleft()
    if cur_vertex == start:
        continue
    
    for weight, next_vertex in edge_reverse[cur_vertex]:
        if cur_time - weight == max_time[next_vertex] and cur_vertex not in lane[next_vertex]:
            # �׷����� a->b �϶� b������ �ִ���-(a���� b�κ��� a�� ���� ���) == a������ �ִ����� ���
            # ��, a-b���� �����ʰ� �����ϴ� ��� and �ش� ������ �������� ���� ���
            total_lane += 1
            lane[next_vertex].append(cur_vertex)    # �ߺ� ������ ���� ���� �߰�
            dq.append((max_time[next_vertex], next_vertex))
            
print(max_time[end])
print(total_lane)