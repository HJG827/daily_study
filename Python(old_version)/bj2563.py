# 색종이

N = int(input())
arr = [[0]*101 for _ in range(101)]
ans = 0

for i in range(N):
    r, c = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[r+i][c+j] = 1
    

for r in range(101):
    for c in range(101):
        if arr[r][c]:
            ans += 1

print(ans)