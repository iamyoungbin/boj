def isPromising(n):
    for i in range(n):
        if queen[n]==queen[i] or abs(queen[n] - queen[i])== n-i:    # 같은 열에 위치하거나 대각선에 위치하면
            return False

    return True

def dfs(n):
    global cnt
    if n == N:  # 해답에 도달하면
        cnt+=1
        return

    for i in range(N):
        queen[n] = i
        if isPromising(n):
            dfs(n+1)

N = int(input())
cnt = 0
queen = [0] * N
dfs(0)

print(cnt)
