import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def find(x):
    if x != port[x]:
        port[x] = find(port[x])

    return port[x]

G = int(input())
P = int(input())

port = [i for i in range(G+1)]
airplane = []
for _ in range(P):
    airplane.append(int(input()))

cnt = 0
for ap in airplane:
    p = find(ap)
    if p == 0:
        break
    port[p] = p-1
    cnt += 1

# print(port)
print(cnt)