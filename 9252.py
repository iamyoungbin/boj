import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

lcs = [["" for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str1[j-1] == str2[i-1]:
            lcs[i][j] = lcs[i-1][j-1] + str1[j-1]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
                
print(len(lcs[-1][-1]))
if len(lcs[-1][-1]) != 0:    
    print(lcs[-1][-1])