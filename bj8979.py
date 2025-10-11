# 올림픽
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

ans = 1

if arr[0][0] == K:
    print(ans)

for i in range(N-1):
    if (arr[i+1][1], arr[i+1][2], arr[i+1][3]) != (arr[i][1], arr[i][2], arr[i][3]):
        ans = i + 2
    if arr[i+1][0] == K:
        print(ans)
        break