import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

ans = 1
max_side = min(N, M) - 1

if max_side < 1:
    print(ans)

else:
    for d in range(1, max_side + 1):
        for r in range(N - d):
            for c in range(M - d):
                if arr[r][c] == arr[r + d][c] == arr[r][c + d] == arr[r + d][c + d]:
                    ans = (d + 1) ** 2
                    

    print(ans)