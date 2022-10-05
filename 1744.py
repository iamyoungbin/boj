import sys

input = sys.stdin.readline

N = int(input())
low_que = []
high_que = []

sol = 0
for _ in range(N):
    num = int(input())
    if num == 1:
        sol += num
    elif num >= 2:
        high_que.append(num)
    else:
        low_que.append(num)
        
high_que.sort(reverse=True)
low_que.sort()

for i in range(0, len(high_que), 2):
    if i == len(high_que)-1:
        sol += high_que[i]
    else:
        sol += (high_que[i] * high_que[i+1])
        
for i in range(0, len(low_que), 2):
    if i == len(low_que)-1:
        sol += low_que[i]
    else:
        sol += (low_que[i] * low_que[i+1])
        
print(sol)