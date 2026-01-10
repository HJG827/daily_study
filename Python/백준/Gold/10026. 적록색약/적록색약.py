import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

def red_green_same(sr, sc):
    visited[sr][sc] = 1
    q = deque()
    q.append([sr, sc, arr[sr][sc]])

    while q:
        tr, tc, val = q.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and not visited[nr][nc]
            ):
                nval = arr[nr][nc]
                if val == "R" or val == "G":
                    if nval == "R" or nval == "G":
                        visited[nr][nc] = 1
                        q.append([nr, nc, nval])
                elif val == nval:
                    visited[nr][nc] = 1
                    q.append([nr, nc, nval])

def red_green_different(sr, sc):
    visited[sr][sc] = 1
    q = deque()
    q.append([sr, sc, arr[sr][sc]])

    while q:
        tr, tc, val = q.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and not visited[nr][nc]
            ):
                nval = arr[nr][nc]
                if val == nval:
                    visited[nr][nc] = 1
                    q.append([nr, nc, nval])

ans1 = 0
ans2 = 0

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            red_green_different(r, c)
            ans1 += 1

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            red_green_same(r, c)
            ans2 += 1

print(ans1, ans2)
