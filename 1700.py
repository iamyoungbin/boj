# -*- coding: utf-8 -*-
#pypy3
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
schedule = list(map(int, input().split()))

plug = {}   # 전기용품 : 해당 전기용품의 다음 사용 순서
sol = 0
for i in range(K):
    for j in range(i+1, K):
        if schedule[i] == schedule[j]:
            next = j
            break
    else:   # schedule 내에 해당 전기용품 사용이 없으면 마지막 사용순서 할당, K <= 100
        next = 101

    if schedule[i] in plug.keys() or len(plug) < N: # plug 내에 이미 전기용품이 꽂혀 있는 경우 or 플러그가 꽉차지 않은 경우
        pass    # 해당 전기용품 사용순서만 초기화(추가)
    else:
        change = max(plug, key=plug.get)    # 플러그 내에서 가장 나중에 사용되는 전기용품 선택.
        plug.pop(change)    # 플러그에서 뽑음.
        sol += 1

    plug[schedule[i]] = next

print(sol)        