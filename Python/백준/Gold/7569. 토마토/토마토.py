from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[[0] * M for _ in range(N)] for _ in range(H)]
ripe_tomatoes = deque()
ans = 0

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]
 
for h in range(H):
    for r in range(N):
        boxes[h][r] = list(map(int, input().split()))

def check_tomatoes(arr):
    result = 1
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 0:
                    result = 0
                elif arr[h][r][c] == 1:
                    ripe_tomatoes.append([h, r, c])

    return result

if check_tomatoes(boxes):
    print(0)

else:
    while ripe_tomatoes:
        for _ in range(len(ripe_tomatoes)):
            th, tr, tc = ripe_tomatoes.popleft()
            for dr, dc in zip(dir_r, dir_c):
                nr = tr + dr
                nc = tc + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                ):
                    if boxes[th][nr][nc] == 0:
                        boxes[th][nr][nc] = 1
                        ripe_tomatoes.append([th, nr, nc])
            for dh in (-1, 1):
                nh = th + dh
                if 0 <= nh < H:
                    if boxes[nh][tr][tc] == 0:
                        boxes[nh][tr][tc] = 1
                        ripe_tomatoes.append([nh, tr, tc])
        ans += 1

    if check_tomatoes(boxes) == 0:
        print(-1)
    else:
        print(ans - 1)