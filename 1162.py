# -*- coding: utf-8 -*-
import sys
import heapq

def dijkstra(k):
    heap = []
    visited = [[False for _ in range(N+1)] for _ in range(k+1)]
    dist = [[sys.maxsize for _ in range(N+1)] for _ in range(k+1)]

    heapq.heappush(heap, (0, 1, 0)) # ��������� �Ÿ�, ���� ����, ���� ��� Ƚ��
    dist[0][1] = 0

    while heap:
        pd, pv, pk = heapq.heappop(heap)

        if visited[pk][pv] == False:
            visited[pk][pv] = True

            for nd, nv in edge[pv]:
                if dist[pk][pv] + nd < dist[pk][nv]:    # �Ϲ� ���ͽ�Ʈ��
                    dist[pk][nv] = dist[pk][pv] + nd
                    heapq.heappush(heap, (dist[pk][nv], nv, pk))

                if pk < k and dist[pk][pv] <dist[pk+1][nv] :    # pk < k, ���� Ƚ���� �������� ��� ����ġ�� ������ ���� ä�� ���ͽ�Ʈ��
                    dist[pk+1][nv] = dist[pk][pv]
                    heapq.heappush(heap, (dist[pk+1][nv], nv, pk+1))

    min = sys.maxsize
    for i in dist:
        if i[N] < min:
            min = i[N]

    return min

N, M, K = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    edge[v1].append((w, v2))
    edge[v2].append((w, v1))

print(dijkstra(K))