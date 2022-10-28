import sys

input = sys.stdin.readline

weight_num = int(input())
weight = list(map(int, input().split()))
marble_num = int(input())
marble = list(map(int, input().split()))

dp = {}
for w in weight:
    cache = {w:True}
    for k in dp.keys():
        if w+k <= 40000:
            cache[w+k] = True
        if w-k > 0:
            cache[w-k] = True
        if k-w > 0:
            cache[k-w] = True
            
    dp.update(cache)

for m in marble:
    if dp.get(m):
        print("Y", end=" ")
    else:
        print("N", end=" ")