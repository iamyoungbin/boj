import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = input().rstrip()
    n = int(input())
    if n != 0:
        temp = list(map(int, input().replace(',', ' ').lstrip('[').rstrip(']\n').split(' ')))
    else:
        input()
        temp = []
    queue = deque(temp)

    flag = True
    direction = 0
    for c in cmd:
        if c == 'R':
            direction += 1
        elif len(queue) >= 1:
            if direction%2 == 0:
                queue.popleft()
            else:
                queue.pop()
        else:
            print("error")
            flag = False
            break

    if flag == True:
        if direction%2 == 1:
            queue.reverse()

        print("[", end="")
        for i in range(len(queue)):
            if i != len(queue)-1:
                print(queue[i], end=",")
            else:
                print(queue[i], end="")
        print("]")