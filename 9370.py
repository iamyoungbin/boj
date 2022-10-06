import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (dist[start], start))
    
    while heap:
        pd, pn = heapq.heappop(heap)
        
        if pd > dist[pn]:
            continue
        
        for nd, nn in edge[pn]:
            if dist[pn] + nd < dist[nn]:
                dist[nn] = dist[pn] + nd
                heapq.heappush(heap, (dist[nn], nn))
                
    return dist
    
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        edge[a].append((d, b))
        edge[b].append((d, a))
    
    xlist = []
    for _ in range(t):
        xlist.append(int(input()))
        
    sol = []
    s_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    
    for x in xlist:
        if g_dist[h] + s_dist[g] + h_dist[x] == s_dist[x] or g_dist[h] + s_dist[h] + g_dist[x] == s_dist[x]:
            sol.append(x)
        
    sol.sort()
    print(*sol)
    
"""
test case :
1
6 6 2
1 2 3
1 2 1
2 3 2
3 4 1
4 5 2
1 6 4
6 5 1
4
5

ans : 4
"""