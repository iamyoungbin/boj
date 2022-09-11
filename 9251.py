import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

cnt = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str1[j-1] == str2[i-1]:
            cnt[i][j] = cnt[i-1][j-1] + 1
        else:
            cnt[i][j] = max(cnt[i-1][j], cnt[i][j-1])

# for c in cnt:
#     print(*c)

print(cnt[-1][-1])