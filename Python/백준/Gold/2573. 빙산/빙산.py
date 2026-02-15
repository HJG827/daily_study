import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

ice = []
for r in range(N):
    for c in range(M):
        if arr[r][c] > 0:
            ice.append((r, c))

def bfs(sr, sc, visited):
    q = deque()
    q.append((sr, sc))

    visited[sr][sc] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dir_r[d]
            nc = c + dir_c[d]

            if (
                0 <= nr < N
                and 0 <= nc < M
                and arr[nr][nc]
                and not visited[nr][nc]
            ):
                visited[nr][nc] = 1
                q.append((nr, nc))

def count_glacier():
    visited = [[0] * M for _ in range(N)]
    count = 0

    for r, c in ice:
        if not visited[r][c]:
            bfs(r, c, visited)
            count += 1

    return count

ans = 0

while True:
    cnt = count_glacier()

    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        print(ans)
        break

    melt = [[0] * M for _ in range(N)]

    for r, c in ice:
        water = 0
        for d in range(4):
            nr = r + dir_r[d]
            nc = c + dir_c[d]
            if (
                0 <= nr < N
                and 0 <= nc < M
                and arr[nr][nc] == 0
            ):
                water += 1
        
        melt[r][c] = water

    new_ice = []
    for r, c in ice:
        arr[r][c] = max(0, arr[r][c] - melt[r][c])
        if arr[r][c] > 0:
            new_ice.append((r, c))

    ice = new_ice
    ans += 1