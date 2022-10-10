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
        if cur_time + weight > max_time[next_vertex]:   # 다음 정점으로 가는 최대비용 값 업데이트
            max_time[next_vertex] = cur_time + weight
            
        if degree[next_vertex] == 0:    # 모든 진입 차수 중 시작지점부터 최대비용으로 진입하는 간선 이용
            dq.append((max_time[next_vertex], next_vertex))

dq = deque()
dq.append((max_time[end], end))
lane = [[] for _ in range(n+1)] # 간선 이용에 대한 중복 계산 방지
total_lane = 0
while dq:   # 도착지점으로부터 출발지점까지 역방향으로 bfs
    cur_time, cur_vertex = dq.popleft()
    if cur_vertex == start:
        continue
    
    for weight, next_vertex in edge_reverse[cur_vertex]:
        if cur_time - weight == max_time[next_vertex] and cur_vertex not in lane[next_vertex]:
            # 그래프가 a->b 일때 b까지의 최대비용-(a에서 b로부터 a로 가는 비용) == a까지의 최대비용인 경우
            # 즉, a-b간에 쉬지않고 가야하는 경우 and 해당 간선이 세어지지 않은 경우
            total_lane += 1
            lane[next_vertex].append(cur_vertex)    # 중복 방지를 위한 간선 추가
            dq.append((max_time[next_vertex], next_vertex))
            
print(max_time[end])
print(total_lane)