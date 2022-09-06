import sys

input = sys.stdin.readline

N = int(input())
crane = sorted(map(int, input().split()), reverse=True)
M = int(input())
box = sorted(map(int, input().split()), reverse=True)

time = 0
if box[0] > crane[0]:
    time = -1
else:
    while box:
        for c in crane:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break

        time += 1
            
print(time)